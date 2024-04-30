import reflex as rx
from codemeonline.API.judgezeroApi import JudgeZeroApi
from codemeonline.States.EditedCode import EditedCode
from codemeonline.States.Languages import dropdown_lang, LanguagesState


class CodeArea(rx.Component):
    '''the text area where the code will be edited'''

    library= "@monaco-editor/react"
    tag= "Editor"
    is_default=True


    """Default programming language"""
    defaultLanguage: str = "python"
    defaultValue: str = "#Type your code here"
    language: rx.Var[str] = ""
    value: rx.Var[str] = ""
    theme: str = "vs-dark"
    width: str = "100%"
    options: dict = {"readOnly" : "false", "lineNumbers": "on"}
    on_change: rx.EventHandler[lambda e0: [e0]]
        

codearea = CodeArea.create


def desktop_code_card() -> rx.Component:
    return rx.desktop_only(
        rx.card(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.button('Clear', on_click=lambda: EditedCode.clear_input, type= 'reset'),
                        rx.button(rx.icon('play'),'Run', on_click=[lambda: EditedCode.compilecode]),
                        rx.menu.root(
                            rx.menu.trigger(
                                rx.button(rx.icon("square-code"),"Language", variant="soft"),
                            ),
                                rx.menu.content(
                                        rx.foreach(LanguagesState.languages, dropdown_lang)
                                ),
                        ),
                    ),
                    rx.hstack(
                        rx.vstack(
                            rx.text("Input", size="2"),
                            codearea(value= EditedCode.value, language= EditedCode.language_name, on_change = EditedCode.changetext),
                            width="100%",
                            height="100%",
                            ),
                            
                        rx.vstack(
                            rx.text("Output", size="2"),
                            codearea(value=EditedCode.output, language= EditedCode.language_name, defaultValue="", options={"readOnly":"true", "lineNumbers": "off"}),
                            width="100%",
                            height="100%",
                            ),
                        width="100%",
                        height="100%",
                    ),
                width="100%",
                ),
            height='30rem',
            width = '100%',
            ),
            width='100%',
    ),
    width='100%',
)


def code_area():
    return desktop_code_card()

