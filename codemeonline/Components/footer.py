import reflex as rx

def footer () -> rx.Component:
    return rx.vstack(
        rx.divider(size='4'),
        rx.hstack(
            rx.text('CodeXme', weight='medium', padding='0.3rem'),
            rx.button(
                rx.icon('Github'),
                on_click=lambda: rx.redirect('https://github.com/Gioak1993/CodeXme'),
                radius='small',
                padding='0.3rem',
            ),
            rx.spacer(),
            rx.text('This is an ongoing project, more features to come', size='1', text_align='center',),
            padding='1rem',
            align='start',
            width='100%',      
        ),       
        align='start',
        width='100%',
        padding_right='2rem',
    )