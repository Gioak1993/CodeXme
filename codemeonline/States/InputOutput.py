import reflex as rx 
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
                    rx.input(
                        placeholder = "Type your input for one case here", 
                        disabled = InputOutput.editable, 
                        on_change = CreateProblem.set_input_case, 
                        radius = 'small',
                    ),
                    rx.text('Output'),
                    rx.input(
                            placeholder = "Type your output for one case here", 
                            disabled = InputOutput.editable, 
                            on_change = CreateProblem.set_output_case,
                            radius = 'small',
                            ),
                    rx.button('Confirm Case', 
                            on_click = [CreateProblem.add_input_output],
                            margin = '0.3rem',
                            
                    ),
                    text_align = 'center',
                    align = 'center',
                    width = '30%',
                ),
                align = 'center',
                width = "100%",
)


def input_output_pair() -> rx.Component:
    return rx.vstack(
                rx.foreach(InputOutput.input_output_field, input_output_item),
                inputs_output_table(),
                rx.button('Finish', 
                        on_click = lambda: rx.redirect('/challenges'),
                        margin_right = 'auto',
                        margin_left = 'auto',
                        margin_top = '0.5rem',
                ),
                width = '100%',
    )

##table for showing the current input-outputs in the database 

def input_output_list (item) -> rx.Component:

    return rx.table.row(
                rx.table.row_header_cell(item.input_data, style = {"width": "25%"}),
                rx.table.cell(item.expected_output, style = {"width": "25%"}),
                rx.table.cell(
                    rx.button(
                        rx.icon("trash-2"), 
                    on_click = CreateProblem.delete_input_output(item.id),
                    ),
                    style={"width": "10%"},
                ),
                width = '50%',    
)

def inputs_output_table() -> rx.Component:

    return rx.flex(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell('Input', style = {"width": "25%"}),
                            rx.table.column_header_cell('Output', style = {"width": "25%"}),
                            rx.table.column_header_cell('Delete pair', style = {"width": "10%"}),                       
                        ),
                    ),
                    rx.table.body(
                        rx.foreach(CreateProblem.current_input_output, input_output_list),
                    ),
                    variant = 'ghost',
                    width = '50%',
                ),
                direction = "column",
                spacing = "2",
                width = '100%',
                align = 'center',
)