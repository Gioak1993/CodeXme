"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
import reflex as rx
from .Pages.index import index
from .Pages.editor import editor
from .Pages.login import login
from .Pages.signup import signup
from .Pages.problems import problems, QueryProblems
from .Pages.newproblem import newproblem
from .States.CategoryState import CategoryState
from .States.CreateProblem import CreateProblem
from .SqlModels.models import * 


## Ensure that your main app module is importing your Model objects, otherwise Reflex will not know they are there.


docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    


app = rx.App(
    theme=rx.theme(
        has_background=True,
        radius="full",
        accent_color="cyan",
    ),
)
app.add_page(index, route='/')
app.add_page(editor, route='/playground')
app.add_page(login, route='/login')
app.add_page(signup, route='/signup')
app.add_page(problems,  route='/problems', on_load=QueryProblems.get_all_problems)
app.add_page(newproblem,  route='/newproblem', on_load=[CategoryState.get_categories, CreateProblem.get_user])

