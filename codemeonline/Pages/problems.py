import reflex as rx 
from codemeonline.Components.navbar import navbar
from ..States.Auth import AuthState

def problems () -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.cond(AuthState.logged_in,
                rx.button("Create a new Problem here!"),
                rx.button("Sign in To create a new problem")),
        padding="1rem",
        )

