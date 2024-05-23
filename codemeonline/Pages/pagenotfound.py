import reflex as rx 
from ..Components.navbar import navbar
from ..Components.footer import footer

def not_found() -> rx.Component:

    return rx.vstack(
            navbar(),
            rx.vstack(
                rx.flex(
                    rx.heading("404", size='9'), # Big 404 text
                    rx.text("Page Not Found", size='6'), # Subtitle
                    rx.link("Go to Home", href="/"),
                    direction='column',
                    margin_top='auto',
                    margin_bottom = 'auto',
                    align='center'
                ),
                height="80vh",
                
            ),
            footer(), 
            spacing="4",
            align="center",
            justify="center",
            padding='1rem',
)