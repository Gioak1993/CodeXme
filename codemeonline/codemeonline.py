"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
import reflex as rx
from .Pages.index import index
from .Pages.editor import editor
from .Pages.login import login
from .Pages.signup import signup
from .Pages.problems import problems
from .Pages.newproblem import newproblem
from .Pages.problemchallenge import problem_challenge
from .States.CategoryState import CategoryState
from .States.CreateProblem import CreateProblem
from .States.QueryProblems import QueryProblems, GetProblem
from .SqlModels.models import * 


## Ensure that your main app module is importing your Model objects, otherwise Reflex will not know they are there.



class State(rx.State):
    """The app state."""

app = rx.App(
    theme=rx.theme(
        has_background=True,
        radius="full",
        accent_color="cyan",
    ),
    stylesheets=['https://fonts.googleapis.com/css2?family=Roboto:ital&display=swap'], #style={"font_family":"Roboto, sans-serif"}
)
app.add_page(index, route='/', title="Codexme, your web to try, practice and learn new programming languages!")
app.add_page(editor, route='/playground')
app.add_page(login, route='/login')
app.add_page(signup, route='/signup')
app.add_page(problems,  route='/challenges', on_load=QueryProblems.get_all_problems)
app.add_page(newproblem,  route='/newproblem', on_load=[CategoryState.get_categories, CreateProblem.get_user])
app.add_page(problem_challenge, route='challenges/[handle-title]', on_load= [GetProblem.get_problem_by_handle_title,  GetProblem.extract_input_output])

