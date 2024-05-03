import reflex as rx

def light_dark_button():
    return rx.color_mode_cond(
                            rx.color_mode.button(                       
                                rx.color_mode.icon(),
                                color='black',
                                background_color='#EEEEEE',
                                size='2',
                            ),
                            rx.color_mode.button(                       
                                rx.color_mode.icon(),
                                background_color='#111111',
                                size='2',
                            ),
            )
