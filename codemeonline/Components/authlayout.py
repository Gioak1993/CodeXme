"""Shared auth layout."""

import reflex as rx
from .container import container


def auth_layout(*args):
    """The shared layout for the login and sign up pages."""
    return rx.box(
        container(
            rx.vstack(
                rx.heading("Welcome to CodexMe!", size = "8"),
                rx.heading("Sign in or sign up to get started.", size = "8"),
                align="center",
            ),
            
            *args,
            border_top_radius = "10px",
            box_shadow = "0 4px 60px 0 rgba(0, 0, 0, 0.08), 0 4px 16px 0 rgba(0, 0, 0, 0.08)",
            display = "flex",
            flex_direction = "column",
            align_items = "center",
            padding_top = "36px",
            padding_bottom = "24px",
            spacing = "4",
        ),
        width = "100%",
        height = "100vh",
        padding_top = "40px",
        background = "url(bg.svg)",
        background_repeat = "no-repeat",
        background_size = "cover",
    )