"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
import reflex as rx
from .Pages.index import index
from .Pages.editor import editor
from .Pages.login import login
from .Pages.signup import signup
from .Pages.problems import problems
from .SqlModels.models import * 
# from .States.Logged import Log
## Ensure that your main app module is importing your Model objects, otherwise Reflex will not know they are there.


docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""


app = rx.App()
app.add_page(index, route='/')
app.add_page(editor, route='/editor')
app.add_page(login, route='/login')
app.add_page(signup, route='/signup')
app.add_page(problems,  route='/problems')
