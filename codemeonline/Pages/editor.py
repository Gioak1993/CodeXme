import reflex as rx
from codemeonline.Components.codeArea import code_area
from codemeonline.Components.navbar import navbar
from ..Components.footer import footer

def editor ()-> rx.Component:
    return rx.vstack(
        navbar(),
        rx.heading('Playground', 
                   as_='h1', 
                   align='center', 
                   size='8'),
        rx.markdown('''Whether you're at your desktop or on the go, you can dive into coding.\
                        Learn from your phone or tablet—it's all within reach. Our playground is here for you,
                        whether you're honing your skills or exploring a new language.''',
                        as_='p',
                        size='7',
        ),
        code_area(),
        footer(),
        width='100%',
        padding = "1rem",
        align='center',
    )
