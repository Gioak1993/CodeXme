import reflex as rx 
from ..SqlModels.models import TestCase
from ..States.CreateProblem import CreateProblem

class InputOutput(rx.State):

    input_output_field: list[str] = [' ']
    editable: bool
    show_section: bool = False

    #add a field when the user wants to add more than one category
    
    def change_visibility(self):
        
        self.show_section = not self.show_section

    def add_field(self):
        self.input_output_field.append('value')
    
    def delete_field(self):
        del self.input_output_field[-1]

    def toggle_editable(self): 
        self.editable = not self.editable


def input_output_item(test_item) -> rx.Component:
    return  rx.vstack(
                rx.card(
                    rx.text('Input'),
                    rx.input(placeholder="Type your input for one case here", disabled=InputOutput.editable, on_change=CreateProblem.set_input_case),
                    rx.text('Output'),
                    rx.input(placeholder="Type your output for one case here", disabled=InputOutput.editable, on_change=CreateProblem.set_output_case),
                    rx.button('Confirm Case', on_click=[CreateProblem.add_input_output, InputOutput.toggle_editable]),
                    text_align='center',
                    align='center',
                ),
                align='center',
)


def input_output_pair() -> rx.Component:
    return rx.vstack(
                rx.foreach(InputOutput.input_output_field, input_output_item),
                rx.hstack(
                rx.button("Add", on_click=InputOutput.add_field),
                rx.button("Delete", on_click=InputOutput.delete_field, color_scheme='red'),),
                align='center',
    )