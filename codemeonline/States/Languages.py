import reflex as rx
from codemeonline.API.judgezeroApi import JudgeZeroApi
from codemeonline.States.EditedCode import EditedCode

class LanguagesState(rx.State):

    languages: dict[str, int] = {
        "Python": 92,
        "Javascript": 93,
        "TypeScript": 94,
        "Swift": 83,
        "Assembly": 45,
        "Bash": 46,
        "C" : 75,
        "C++" : 76,
        "C#" : 51,
        "COBOL": 77,
        "D": 56,
        "Dart": 90,
        "Elixir": 57,
        "Erlang": 58,
        "F#": 87,
        "Fortran": 59,
        "Go" : 95,
        "Grovy": 88,
        "Haskell": 61,
        "Kotlin": 78,
        "Lua": 64,
        "Objective-C": 79,
        "Octave": 66,
        "Perl": 85,
        "R": 80,
        "Ruby": 72,
        "Scala": 81,

    }

def dropdown_lang(lang):

    return rx.menu.item(lang[0], on_select = [EditedCode.setlanguage_name(lang[0]), EditedCode.setlanguage_code(lang[1])])