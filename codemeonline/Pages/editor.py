import reflex as rx
from codemeonline.Components.codeArea import code_area
from codemeonline.Components.navbar import navbar

def editor ()-> rx.Component:
    return rx.vstack(
        navbar(),
        code_area(),
        width='100%',
        padding = "1rem",
    )
