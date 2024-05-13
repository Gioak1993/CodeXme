import reflex as rx
from codemeonline.API.judgezeroApi import JudgeZeroApi
from .QueryProblems import GetProblem
import time

class EditedCode(rx.State):


    code:str = ""
    output:str = ""
    language_id: int = 92
    language_name: str = "python"
    default_value: str = ""
    code_input: str = ""
    correct_submission: bool = False
    
    def changetext(self, new_text:str):

        self.code: str = new_text

    def setlanguage_code (self, lang):

        self.language_id = lang

    def setlanguage_name (self, lang_name):

        self.language_name = lang_name.lower()

    def set_loading(self):
        self.output= "Loading..."

    def compilecode (self):
        
        code_results = JudgeZeroApi(language_id= self.language_id, source_code=self.code)
        results = code_results.get_token()
        if type(results) != type(None):
            stdout = results['stdout']
            stderror = results ['stderr']
            status = results ['status']
            description = status ['description']
            if type(stdout) == str:
                self.output = stdout
            
            elif type(stdout) == type(None):
                self.output = stderror

            else:
                self.output = "The server cant respond right now due to many of requests, wait a few minutes"
        else:
            self.output = "There was an error"

        print(self.output)

    async def run_challenge (self) -> bool:
            
            user_code = await self.get_state(GetProblem)
            compare_code = f'''{self.code}
        
        
print({user_code.solutions}, sep=",")
            '''
        
            self.code = compare_code
            
            print(self.code)




