import reflex as rx
from ..Components.signupbutton import signup_button
from ..Components.light_dark_button import light_dark_button


def navbar() -> rx.Component:
     return rx.stack(
          dekstop_navbar(),
          mobile_navbar(),
          width='100%',
     )



def dekstop_navbar() -> rx.Component:

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
                    rx.text( 'Playground',
                        on_click= rx.redirect('/playground'),
                        cursor='pointer',
                    ),
                    rx.text('Challenges',
                        rx.badge("beta", 
                                 margin="0.2rem",),
                        on_click= rx.redirect('/challenges'),
                        cursor='pointer',
                        
                    ),
                    light_dark_button(),
                    signup_button(),
                    width='100%',
                    spacing='7',
                    
                    ),
                    width = "100%"              
            )

def mobile_navbar() ->rx.Component:

    return rx.mobile_and_tablet(
                    rx.hstack(
                        rx.heading("Codexme", size='6',
                                    on_click= lambda : rx.redirect('/'),
                                    cursor='pointer',
                                    ),
                        rx.spacer(),
                        light_dark_button(),
                        rx.menu.root(
                            rx.menu.trigger(
                                rx.button(
                                    rx.icon('chevron-down'),
                                    size='2',
                                ),
                            ),
                            rx.menu.content(
                                rx.menu.item('Home', on_click=lambda: rx.redirect('/')),
                                rx.menu.item('Playground', on_click=lambda: rx.redirect('playground')),
                                rx.menu.item('Challenges',
                                            rx.badge("beta", 
                                                    margin="0.2rem",
                                            ), 
                                            on_click=lambda: rx.redirect('challenges')),
                                signup_button(),
                                size='2',
                                text_align='center',
                                align='center',
                                side='bottom',
                            )
                        )
                    ),
                    width='100%',
                    padding = "1.5rem",
            )



        