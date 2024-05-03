import reflex as rx
from codemeonline.API.judgezeroApi import JudgeZeroApi

class EditedCode(rx.State):


    value:str = ""
    output:str = ""
    language_id: int = 92
    language_name: str = "python"
    default_value: str = ""
    

    def changetext(self, new_text:str):
        
        self.value: str = new_text
        print (self.value)
        

    def clear_input (self):

        self.value = ""
        print (self.value)

    def setlanguage_code (self, lang):

        self.language_id = lang
        print (self.language_id)

    def setlanguage_name (self, lang_name):
        self.language_name = lang_name.lower()
        print (self.language_name)

    def compilecode (self):
        
        code_results = JudgeZeroApi(language_id= self.language_id, source_code=self.value)
        results = code_results.get_token()
        if type(results) != type(None):
            stdout = results['stdout']
            stderror = results ['stderr']
            if type(stdout) == str:
                self.output = stdout
                print (stdout, type(stdout))
            elif type(stdout) == type(None):
                self.output = stderror
                print (stdout, type(stderror))
        else:
            self.output = "There was an error"
