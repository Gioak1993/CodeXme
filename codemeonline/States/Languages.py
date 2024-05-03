import reflex as rx
from codemeonline.API.judgezeroApi import JudgeZeroApi
from codemeonline.States.EditedCode import EditedCode

class LanguagesState(rx.State):

    languages: dict[str, int] = {
        "Python": 92,
        "Javascript": 63,
        "Swift": 83,
    }

def dropdown_lang(lang):

    return rx.menu.item(lang[0], on_select = [EditedCode.setlanguage_name(lang[0]), EditedCode.setlanguage_code(lang[1])])