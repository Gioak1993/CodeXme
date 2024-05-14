import reflex as rx 
from sqlmodel import select
from datetime import datetime, UTC
from ..States.CreateProblem import CreateProblem
from ..States.Auth import AuthState
from ..States.InputOutput import InputOutput
from ..Components.category_button import dropdown_category
from ..Components.navbar import navbar
from ..Components.footer import footer
from ..States.InputOutput import input_output_pair



#dropdown difficulty component
def dropdown_difficulty() -> rx.Component:
    return rx.select(
            CreateProblem.difficulty_list,
            placeholder="Select the Difficulty",
            on_change=CreateProblem.set_difficulty,
)

#if the user its not auth show this
def user_not_auth_problem() -> rx.Component:
    return rx.vstack(
            rx.heading("You need to be authenticate to post a new code challenge! click here"),
            rx.button("Sign Up", on_click= lambda: rx.redirect('/signup')),
    )

#if the user is auth show this 
def user_auth_problem() -> rx.Component:
    return  rx.box(
            rx.vstack(
                rx.heading('Title'),
                rx.input(
                    type="text",
                    placeholder="",
                    on_blur=CreateProblem.set_title,
                    width = "70vw",
                ),
                rx.heading('Description'),
                rx.text_area(
                    type="description",
                    placeholder="Type your description here ",
                    on_blur=CreateProblem.set_description,
                    size="3",
                    height= "700px",
                    width = "80%",
                ),
                rx.heading('Difficulty'),
                dropdown_difficulty(),
                rx.heading('Category'),
                dropdown_category(),
                rx.text("Set your number of input variables"),
                rx.select(['1','2','3','4','5'], placeholder="Select input", on_change=CreateProblem.set_number_input_variables),
                rx.text("Set your number of output variables"),
                rx.select(['1','2','3','4','5'], placeholder="Select input", on_change=CreateProblem.set_number_output_variables),
                rx.button("Create Problem", on_click=[CreateProblem.create_problem, InputOutput.change_visibility], size="3",),
                rx.cond(InputOutput.show_section,
                        rx.section(
                            rx.heading('Inputs/Outputs'),
                            rx.text("This section appears after a click"),
                            input_output_pair(),
                        ),
                        rx.text("Once you create the problem, then we are going to store the inputs and outputs")
                ),
                spacing="4",
                align="center",
                width='100%',
            ),
            align_items="start",
            border="1px solid #eaeaea",
            padding="16px",
            width="100%",
            border_radius="8px",
)

def newproblem () -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.cond(AuthState.logged_in, user_auth_problem(), user_not_auth_problem()),
        rx.logo(),
        footer(),
        width="100%",
        padding="1rem",
    )
