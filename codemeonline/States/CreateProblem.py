import reflex as rx 
from sqlmodel import select
from datetime import datetime, UTC
from .Auth import AuthState
from .CategoryState import CategoryState
from ..SqlModels.models import Problem, TestCase

class CreateProblem (rx.State):

    title:str
    description: str
    difficulty: str 
    difficulty_list: list[str] = ["Easy", "Medium", "Hard", "Extreme"]
    input_output: dict
    user_id: str
    category: list[str]
    input_case:str
    output_case:str
    category_data: list[str]

    #take the current user
    async def get_user(self):
        user = await self.get_state(AuthState)
        self.user_id = user.user_id_cookie
        print(self.user_id)

    #save the data on the Problem database
    async def create_problem (self):

        test_case: dict | None 

        with rx.session() as session:
            self.category_data = await self.get_state(CategoryState)            
            category_problem_list = [item for item in self.category_data.categories if item.name in self.category] 
            problem = Problem(title=self.title, description=self.description, difficulty=self.difficulty, user_id=self.user_id, created_at=datetime.now(UTC), categories=category_problem_list)      
            session.add(problem)
            session.expire_on_commit = False
            session.commit()

    def add_category (self, item: str):

        if item not in self.category:
            self.category.append(item)
            print(self.category)

    def del_category(self):
        if len(self.category) >= 1:
            del self.category[-1]
        else:
            pass
        print(self.category)

    def add_input_output (self):

        if self.input_case == '' or self.output_case:
            pass
        else:
            self.input_output[self.input_case]=self.output_case
            print (self.input_output)

    def set_input_case(self, new_input):

        self.input_case = new_input
        print(self.input_case)

    def set_output_case(self, new_input):

        self.output_case = new_input
        print(self.output_case)

