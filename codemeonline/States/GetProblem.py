import reflex as rx
from ..SqlModels.models import Problem, TestCase
from sqlmodel import select

class GetProblem(rx.State):

    id: int 
    title: str
    handle_title: str #the last part of the url on each problem that will be display. ej: .../problems/handle_title
    description: str
    difficulty: str
    user_id: int  #the user that created the problem
    created_at: str
    input_variables: int  #number of input variables required to formulate and resolve the problem
    output_variables : int  #number of ouput variables required to formulate and resolve the problem
    input_list: list  # all the inputs that are going to be run on the program, they are organized on a list, ex: if you have two input variables, a nums:list and target:int. this is how the list would look like: input variables= [nums, int]
    output_list:list    # all the outputs expected, they are going to be compare with the output generated by the user program. 
    answer: str  
    each_output: str
    solutions: str



    @rx.var
    def item_handle(self) -> str:
        # Capture the handle title form the url
        return self.router.page.params.get("handle_title", "no handle_title")


    
    def get_problem_by_handle_title(self) -> list:
        with rx.session() as session:

            query_problem = session.exec(select(Problem).where(Problem.handle_title == self.item_handle)).first()
            if query_problem:
                self.id = query_problem.id
                self.title = query_problem.title
                self.handle_title = query_problem.handle_title
                self.description = query_problem.description
                self.difficulty = query_problem.difficulty
                self.user_id = query_problem.user_id
                self.created_at = query_problem.created_at
                self.input_variables = query_problem.input_number_variables
                self.output_variables = query_problem.output_number_variables

            query_tests = session.exec(select(TestCase).where(TestCase.problem_id == self.id)).all()

            if query_tests:

                self.input_list = [] #reset the list everytime the function is called so you dont have duplicated values
                self.output_list = [] #reset the list everytime the function is called so you dont have duplicated values
                
                for item in query_tests:
            
                        self.input_list.append(item.input_data)
                        self.output_list.append(item.expected_output)

                # self.each_input=''
                self.solutions=''
                self.each_output=''

                for index, item in enumerate(self.input_list):

                    if index < len(self.input_list) - 1:
                        # self.each_input += f'{item}, '
                        self.solutions +=f'Solution().answer({item}), '
                    else:
                        # self.each_input += f'{item}'
                        self.solutions += f'Solution().answer({item})'
                
                for index, item in enumerate(self.output_list):
                    if index < len(self.output_list) - 1:
                        self.each_output += f'{item},'
                    else:
                        self.each_output += f'{item}'

            
    def extract_input_output (self) ->str:

        name_inputs:str = ""

        for item  in range(self.input_variables):
            
            name_inputs += f', num{item}'
            
        self.answer = f'''class Solution(object):
    def answer(self{name_inputs}):'''
        

        