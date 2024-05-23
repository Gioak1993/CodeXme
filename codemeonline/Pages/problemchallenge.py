import reflex as rx
from ..States.Languages import LanguagesState, dropdown_lang
from ..States.EditedCode import EditedCode
from ..States.GetProblem import GetProblem
from ..States.Results import Results
from ..Components.navbar import navbar
from ..Components.footer import footer
from ..Components.codeArea import CodeArea


codearea= CodeArea.create


def problem_challenge_desktop () -> rx.Component:

    return rx.desktop_only(
        rx.vstack(
                rx.heading(GetProblem.title, padding = '1rem',),
                rx.card(
                    rx.flex(
                        rx.vstack(
                            rx.hstack(
                                rx.button(rx.icon('play'),'Run', on_click=[EditedCode.set_loading, EditedCode.run_challenge, EditedCode.compilecode, Results.get_results]),
                                rx.menu.root(
                                    rx.menu.trigger(
                                        rx.button(rx.icon("square-code"),"Language", variant = "soft"),
                                        ),
                                        rx.menu.content(
                                                rx.foreach(LanguagesState.challenge_language, dropdown_lang)
                                        ),
                                ),
                                rx.spacer(),
                                rx.badge(f'Difficulty: {GetProblem.difficulty}', variant = 'outline',),
                                width='100%',
                            ),
                            rx.hstack(
                                    rx.vstack(
                                        rx.text("Description", 
                                                size = "5", 
                                                weight = 'bold',),
                                        rx.code_block(wrap_long_lines = True, 
                                                    code=GetProblem.description, 
                                                    language = "wiki", 
                                                    show_line_numbers = False, 
                                                    height = "70vh",
                                                    ),
                                        width = "100%",
                                        height = "100%",  
                                        ),
                                    rx.vstack(
                                        rx.text("Your Code", size = "5", weight = 'bold',),
                                        codearea(value = GetProblem.answer, 
                                                language = EditedCode.language_name, 
                                                on_change = EditedCode.changetext,
                                                height = "70vh"
                                                ),
                                                width = "100%",
                                                height = "100%",
                                        ),
                            width = '100%',
                            height = "100%",
                        ),
                    
                    rx.heading('Your result', as_ = 'h4'),
                        rx.cond(Results.results,
                            rx.badge(Results.display_result, color_scheme = "green"),
                            rx.badge(Results.display_result, color_scheme = "red"),
                        
                        ),
                        align = 'center',
                        width = '100%',
                        height = 'auto',
                        min_height = '100%',
                        ),
                    flex_wrap = "wrap",
                    ),
                width = '100%',
                ),
                align= 'center',
        ),
        width = '100%',
)



def problem_challenge_mobile () ->rx.Component:

    return rx.mobile_and_tablet(
        rx.vstack(
                rx.heading(GetProblem.title, padding = '1rem',),
                rx.card(
                    rx.flex(
                        rx.vstack(
                            rx.hstack(
                                rx.button(rx.icon('play'),'Run', on_click = [EditedCode.set_loading, EditedCode.run_challenge, EditedCode.compilecode, Results.get_results]),
                                rx.menu.root(
                                    rx.menu.trigger(
                                        rx.button(rx.icon("square-code"),"Language", variant = "soft"),
                                        ),
                                        rx.menu.content(
                                                rx.foreach(LanguagesState.challenge_language, dropdown_lang)
                                        ),
                                ),
                                rx.spacer(),
                                rx.badge(f'Difficulty: {GetProblem.difficulty}', variant = 'outline',),
                                width='100%',
                            ),
                            rx.tabs.root(
                                    rx.tabs.list(
                                        rx.tabs.trigger("Description", value = "description"),
                                        rx.tabs.trigger("Your Code", value = "your code")
                                    ),
                                        rx.tabs.content(
                                            rx.code_block(wrap_long_lines = True, 
                                                        code = GetProblem.description, 
                                                        language = "wiki", 
                                                        show_line_numbers = False,
                                                        height = "60vh", 
                                                        ),
                                            value="description" 
                                        ),
                                        rx.tabs.content(
                                            codearea(value = GetProblem.answer, 
                                                    language = EditedCode.language_name, 
                                                    on_change = EditedCode.changetext),
                                                    value = "your code",
                                                    width = "100%",
                                                    height = "60vh",
                                        ),
                            default_value = "description",
                            width = "100%",
                            height = "100%", 
                            ),
                            rx.heading('Your result', as_='h4'),
                            rx.cond(Results.results,
                                rx.badge(Results.display_result, color_scheme = "green"),
                                rx.badge(Results.display_result, color_scheme = "red"),
                        
                            ),
                        align = 'center',
                        width = '100%',
                        height = 'auto',
                        min_height = '100%',
                        ),
                flex_wrap = "wrap",
                width = "100%",
                ),
            width = '100%',
            ),  
        align = 'center',
        width = '100%',
        ),
    width = '100%',
)

def problem_challenge () -> rx.Component:

    return rx.vstack(
            navbar(),
            rx.cond(GetProblem.is_loaded, 
                rx.vstack(
                    problem_challenge_desktop(),
                    problem_challenge_mobile(),
                    width = "100%",
                ),
                rx.vstack(
                    rx.spinner(size='3', margin_top = 'auto', margin_bottom = 'auto'),
                    align='center',
                    height = "80vh",
                ),
            ),
            rx.logo(),
            footer(),
            align = 'center',
            padding = '1rem',
            width = '100%',
)