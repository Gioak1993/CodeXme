import reflex as rx
from ..States.Auth import AuthState

def signup_button() -> rx.Component:
    return rx.cond(AuthState.logged_in,
                rx.button("Log Out", on_click = lambda: AuthState.logout),
                rx.button("Sign In", on_click = lambda: rx.redirect('/login')),
)

