import reflex as rx 
from codemeonline.Components.navbar import navbar
from codemeonline.Components.codeArea import code_area

def index() -> rx.Component:
    return rx.vstack(
            navbar(),
            rx.center(
            rx.theme_panel(),
            rx.vstack(
                rx.hstack(
                    rx.vstack(
                        rx.text("Learn to code!\n Try new challenges and have fun!", size="9", as_="p"),
                        rx.text("Get started by trying a new language below! "),
                        width="50%",
                    
                    ),
                    rx.button(
                        "Check out our docs!",
                        on_click=lambda: rx.redirect("/code"),
                        size="4",
                
                    ),
                    margin="15rem",
                    width="100%",
                ),
                code_area(),
                rx.logo(),
                align="center",
                spacing="7",
                font_size="2em",
        ),
        
        width = "100%",
    ),
    width="100%",
    min_height="100vh",
    padding="1rem",
)