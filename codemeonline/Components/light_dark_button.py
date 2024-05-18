import reflex as rx

def light_dark_button():
    return rx.color_mode_cond(
                            rx.color_mode.button(                       
                                color = 'black',
                                background_color = '#EEEEEE',
                                size = '2',
                            ),
                            rx.color_mode.button(                       
                                background_color = '#111111',
                                size = '2',
                            ),
)
