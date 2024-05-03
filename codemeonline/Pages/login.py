import reflex as rx
from codemeonline.Components.authlayout import auth_layout
from codemeonline.States.Auth import AuthState
from codemeonline.Components.navbar import navbar
from ..Components.footer import footer

def login():
    """The login page."""
    return rx.vstack(
        navbar(),
        auth_layout(
        rx.box(
            rx.vstack(
                rx.input(
                    type="email",
                    placeholder="Email",
                    on_blur=AuthState.set_email,
                    size="3",
                ),
                rx.input(
                    type="password",
                    placeholder="Password",
                    on_blur=AuthState.set_password,
                    size="3",
                ),
                rx.button("Log in", on_click=AuthState.login, size="3", width="5em"),
                spacing="4",
                align="center",
            ),
            align_items="left",
            border="1px solid #eaeaea",
            padding="16px",
            width="400px",
            border_radius="8px",
        ),
        rx.text(
            "Don't have an account yet? ",
            rx.link("Sign up here.", href="/signup"),
            color="gray",
        ),
        
    ),
    footer(),
    min_height="100vh",
    padding="1rem",
    width="100%",
)