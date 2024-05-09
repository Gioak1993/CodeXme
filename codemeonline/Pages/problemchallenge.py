import reflex as rx
from ..States.QueryProblems import QueryProblems, GetProblem
from ..States.Languages import LanguagesState, dropdown_lang
from ..States.EditedCode import EditedCode, GetProblem
from ..Components.navbar import navbar
from ..Components.footer import footer
from ..Components.codeArea import CodeArea

codearea= CodeArea.create


class Results(rx.State):

    results:bool = False

    async def get_results(self):

        editecode = await self.get_state(EditedCode)
        getproblem = await self.get_state(GetProblem)
        if editecode.output.strip() == getproblem.each_output.strip():
            self.results = True

        print (editecode.output, getproblem.each_output)


def problem_challenge () ->rx.Component:

    return rx.desktop_only(
        rx.vstack(
                navbar(),
                rx.heading(GetProblem.title),
                rx.card(
                    rx.flex(
                        rx.vstack(
                            rx.hstack(
                                rx.button(rx.icon('play'),'Run', on_click=[EditedCode.set_loading, EditedCode.run_challenge, EditedCode.compilecode, Results.get_results]),
                                rx.menu.root(
                                    rx.menu.trigger(
                                        rx.button(rx.icon("square-code"),"Language", variant="soft"),
                                        ),
                                        rx.menu.content(
                                                rx.foreach(LanguagesState.languages, dropdown_lang)
                                        ),
                                ),
                                rx.spacer(),
                                rx.badge(f'Difficulty: {GetProblem.difficulty}', variant='outline',),
                                width='100%',
                            ),
                            rx.hstack(
                                    rx.vstack(
                                        rx.heading("Description", size="2", as_='h3'),
                                        codearea(value=GetProblem.description, language="cobol", options = {"readOnly" : "false", "lineNumbers": "off", "minimap": {"enabled": "false"}}, line=5 ),
                                        width="100%",
                                        height="100%",
                                        ),
                                    rx.vstack(
                                        rx.text("Your Code", size="2"),
                                        codearea(value = GetProblem.answer, language=EditedCode.language_name, on_change=EditedCode.changetext),
                                        width="100%",
                                        height="100%",
                                        ),
                            width='100%',
                            height="100%",
                        ),
                    rx.heading('Your result', as_='h4'),
                        rx.cond(Results.results,
                            rx.badge("Congratulations! you made it", color_scheme="green"),
                            rx.badge("Waiting for your code or you have some mistake", color_scheme="red"),
                        ),
                    width='100%',
                    height='90vh',
                    ),
                    width='100%',
                    height='100%',
                    ),
                    width="100%",
                    
                ),



                footer(),
                align='center',
                padding='1rem',
                width='100%',
                min_height='100vh'

    ),
    width='100%',
    min_height='100vh',
)