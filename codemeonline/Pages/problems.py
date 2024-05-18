import reflex as rx 
from codemeonline.Components.navbar import navbar
from ..Components.footer import footer
from ..Components.problems_table import problems_table
from ..States.Auth import AuthState
from sqlmodel import select


def problems () -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.heading('Lets practice together! Lets build a community!', 
                as_ = "h1", 
                size = '7', 
                padding = '1rem', 
                text_align = 'center',),
        rx.text('The developer world has made huge advances throught the years thanks to open source projects, free online courses and so much more, lets continue to do su much improvement, if you know coding chellenges dont be afraid to share them here!', 
                size = '6', 
                as_ = 'p', 
                width = "90%", 
                margin = '1rem',
                text_align = 'justify',),
        rx.callout(
            "Currently the challenges are only available on Python, we are working to implement more languages",
            icon = "info",
            color_scheme = "red",
            margin = "0.3rem",
            variant = 'outline',
        ),
        problems_table(),
        rx.cond(AuthState.logged_in,
                rx.button("Create a new Problem here!", 
                        on_click = lambda: rx.redirect('/newproblem'), 
                        margin = '1rem'),
                rx.button("Sign in To create a new problem", 
                        on_click = lambda: rx.redirect('/login'), 
                        margin = '1rem',),
        ),
        rx.logo(),
        footer(),
        
        padding = "1rem",
        align = 'center',
)

