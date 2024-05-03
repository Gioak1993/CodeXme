import reflex as rx 
from codemeonline.Components.navbar import navbar
from codemeonline.Components.codeArea import code_area
from ..Components.footer import footer

def index() -> rx.Component:
    return rx.vstack(
            navbar(),
            rx.center(
            rx.vstack(
                rx.flex(
                    rx.flex(
                        rx.text("Learn to code! Try new challenges and have fun!", as_="p", weight='bold', size='9', text_align='center',),
                        rx.text("Get started by trying a new language below!", text_align='center',),
                        rx.button(
                        "Check the playground!",
                        on_click=lambda: rx.redirect("/playground"), 
                        width= '30%',
                        text_align='center',
                        padding='2rem',
                        margin_top='2rem',
                        ),
                    width=['100%','100%','90%','80%','60%'],
                    margin_top='auto',
                    margin_bottom='auto',
                    direction='column',
                    align='center',
                    ),
                    rx.desktop_only(
                    rx.avatar(
                            src='/owldesktop.jpeg', 
                            width='90%',
                            height='auto',
                            margin_top='auto',
                            margin_bottom='auto',
                    ),
                    width='40%',
                    ),

                    width='100%',
                    padding='2rem',
                    margin="1rem",
                    direction='row',
                    align='center',
                ),
                code_area(),
                rx.text('''Our vision is to democratize access to technology and opportunities, empowering individuals from all 
                        walks of life to harness the power of coding and innovation. By providing accessible online tools and resources, 
                        Codexme aim to break down barriers and unlock the potential of every aspiring coder, regardless of their background, location or resources. ''',
                        as_='p',
                        text_align='justify',
                        size='7', 
                        ),
                rx.logo(),
                align="center",
                spacing="7",
                font_size="2em",
        ),
        
        width = "100%",
    ),
    footer(),
    width="100%",
    min_height="100vh",
    padding="1rem",
)