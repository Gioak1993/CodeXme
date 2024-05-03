import reflex as rx
from codemeonline.API.judgezeroApi import JudgeZeroApi
from codemeonline.States.EditedCode import EditedCode

class LanguagesState(rx.State):

    languages: dict[str, int] = {
        "Python": 92,
        "Javascript": 63,
        "TypeScript": 94,
        "Swift": 83,
        "Assembly": 45,
        "Bash": 46,
        "C" : 75,
        "C++" : 76,
        "C#" : 51,
        "COBOL": 77,
        "Dart": 90,
       "Go" : 60,
       "Ruby": 72,


    }

def dropdown_lang(lang):

    return rx.menu.item(lang[0], on_select = [EditedCode.setlanguage_name(lang[0]), EditedCode.setlanguage_code(lang[1])])