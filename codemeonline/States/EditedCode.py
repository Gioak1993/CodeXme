import reflex as rx
from codemeonline.API.judgezeroApi import JudgeZeroApi
import time

class EditedCode(rx.State):


    value:str = ""
    output:str = ""
    language_id: int = 92
    language_name: str = "python"
    default_value: str = ""
    code_input: str = ""
    
    def changetext(self, new_text:str):

        self.value: str = new_text
        print(self.value)

    def setlanguage_code (self, lang):

        self.language_id = lang

    def setlanguage_name (self, lang_name):

        self.language_name = lang_name.lower()

    def set_loading(self):
        self.output= "Loading..."

    def compilecode (self):
        
        code_results = JudgeZeroApi(language_id= self.language_id, source_code=self.value)
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
