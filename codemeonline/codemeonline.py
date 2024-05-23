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
from .Pages.pagenotfound import not_found 
from .Pages.dashboard import dashboard, Dashboard
from .States.CategoryState import CategoryState
from .States.CreateProblem import CreateProblem
from .States.QueryProblems import QueryProblems
from .States.GetProblem import GetProblem
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
)

app.add_page(index, route = '/', title = "Codexme, your web to try, practice and learn new programming languages!")
app.add_page(editor, route = '/playground', title = "Have fun running different programming languages to see how they work!")
app.add_page(login, route = '/login', title = "Login to CodexMe")
app.add_page(signup, route = '/signup', title = "Sign Up to CodexMe")
app.add_page(problems,  route = '/challenges', on_load = QueryProblems.get_all_problems, title = "Try different challenges to prove your coding skills")
app.add_page(newproblem,  route = '/newproblem', on_load = [CategoryState.get_categories, CreateProblem.get_user], title = "Create a new coding challenge")
app.add_page(problem_challenge, route = 'challenges/[handle_title]', on_load = [GetProblem.reset_is_loaded, GetProblem.get_problem_by_handle_title, GetProblem.extract_input_output], title = GetProblem.title)
# app.add_page(not_found, route='/404', title="404 Not Found", description='The page you are looking for was not found.',)
app.add_custom_404_page(not_found, title="404 Not Found", description='The page you are looking for was not found.', )
# app.add_page(dashboard, route = 'dashboard', on_load = [Dashboard.dashboard])
