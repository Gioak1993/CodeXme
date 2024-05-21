import reflex as rx 
from sqlmodel import select
from sqlalchemy import func
from datetime import datetime, UTC
from .Auth import AuthState
from .CategoryState import CategoryState
from ..SqlModels.models import Problem, TestCase

class CreateProblem (rx.State):

    title:str
    handle_title:str
    description: str
    difficulty: str 
    difficulty_list: list[str] = ["Easy", "Medium", "Hard", "Extreme"]
    user_id: str
    category: list[str]
    input_case:str
    output_case:str
    input_number:str        # the number of variables expected, if you expect two arrays to be inserted then the answer is 2
    output_number: str         # the number of output variables expected. if you expect the program to return 3 different numbers then the answer is 3
    category_data: list[str]
    current_input_output: list[TestCase]

    #take the current user
    async def get_user(self):
        user = await self.get_state(AuthState)
        self.user_id = user.user_id_cookie
        print(self.user_id)

    #save the data on the Problem database
    async def create_problem (self):

        self.category_data = await self.get_state(CategoryState)            
        category_problem_list = [item for item in self.category_data.categories if item.name in self.category]
        self.handle_title = self.title.replace(" ", "-").strip()
        
        with rx.session() as session:
            
            problem = Problem(title=self.title, handle_title=self.handle_title , description=self.description, difficulty=self.difficulty, user_id=self.user_id, created_at=datetime.now(UTC), categories=category_problem_list, input_number_variables=self.input_number, output_number_variables=self.output_number)      
            session.add(problem)
            session.expire_on_commit = False
            session.commit()

    def add_category (self, item: str):

        if item not in self.category:
            self.category.append(item)


    def del_category(self):
        if len(self.category) >= 1:
            del self.category[-1]
        else:
            pass


    def add_input_output (self):

        with rx.session() as session:

            try: 
                query_problem = session.exec(select(Problem).where(Problem.handle_title == self.handle_title)).first()
                max_id = session.exec(func.max(TestCase.id)).scalar() or 0
                next_id = max_id + 1
                input_output = TestCase( id = next_id, input_data = self.input_case, expected_output = self.output_case, problem_id = query_problem.id)
                session.add(input_output)
                session.expire_on_commit = False
                session.commit()

                self.current_input_output = session.exec(select(TestCase).where(TestCase.problem_id  == query_problem.id)).all()
        
            except Exception as e:
                # Handle the exception (e.g., log the error)
                print(f"Error: {e}")
                # Rollback the transaction
                session.rollback()

    def delete_input_output (self, item: int):

        with rx.session() as session:

            query_problem = session.exec(select(Problem).where(Problem.handle_title == self.handle_title)).first()
            input_output = session.exec(select(TestCase).where(TestCase.id == item)).first()
            session.delete(input_output)
            session.commit()

            self.current_input_output = session.exec(select(TestCase).where(TestCase.problem_id  == query_problem.id)).all()

    def set_input_case(self, new_input):

        self.input_case = new_input

    def set_output_case(self, new_input):

        self.output_case = new_input

    def set_number_input_variables(self, number_input_variables):

        self.input_number = number_input_variables

    def set_number_output_variables(self, number_output_variables):

        self.output_number = number_output_variables



