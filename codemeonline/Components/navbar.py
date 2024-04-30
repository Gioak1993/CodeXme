import reflex as rx
from ..Components.signupbutton import signup_button

def navbar() -> rx.Component:
    return rx.desktop_only(
                rx.hstack(
                    rx.heading("CodeXme", size='6',
                       on_click= lambda : rx.redirect('/'),
                       cursor='pointer',
                    ),
                    rx.spacer(),
                    rx.text( 'Home',
                        on_click= rx.redirect('/'),
                        cursor='pointer',
                    ),
                    rx.text( 'Editor',
                        on_click= rx.redirect('/editor'),
                        cursor='pointer',
                    ),
                    rx.text( 'Problems',
                        on_click= rx.redirect('/problems'),
                        cursor='pointer',
                    ),
                    rx.text( 'Learn',
                        on_click= rx.redirect('/code'),
                        cursor='pointer',
                    ),
                    signup_button(),
                    width='100%',
                    
                    ),
                    width = "100%"              
)
        