import reflex as rx 
from codemeonline.Components.navbar import navbar
from ..Components.footer import footer
from ..States.Auth import AuthState
from ..States.QueryProblems import QueryProblems
from ..SqlModels.models import Problem
from sqlmodel import select


def problems_list():

    return rx.data_table(
        data = QueryProblems.problems,
        columns= QueryProblems.columns,
        on_click= rx.redirect("/"),
        margin= '1rem',

    )
def problems () -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.heading('Lets practice together! Lets build a community!', as_="h1", size='7', padding= '1rem',),
        rx.text('The developer world has made huge advances throught the years thanks to open source projects, free online courses and so much more, lets continue to do su much improvement, if you know coding chellenges dont be afraid to share them here!', size='6', as_='p', width = "90%", margin='1rem',),
        problems_list(),
        rx.cond(AuthState.logged_in,
                rx.button("Create a new Problem here!", on_click=lambda: rx.redirect('/newproblem'), margin= '1rem'),
                rx.button("Sign in To create a new problem", on_click=lambda: rx.redirect('/login'), margin= '1rem',),
                
        ),
        rx.logo(),
        footer(),
        
        padding="1rem",
        align='center',
)

