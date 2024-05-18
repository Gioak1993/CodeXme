import reflex as rx
from ..States.QueryProblems import QueryProblems

#Render the list of problems

def problems_list (item) -> rx.Component:

    return rx.table.row(
                rx.table.cell(item.title, 
                            on_click = lambda: rx.redirect(f'/challenges/{item.handle_title}'), 
                            cursor = 'pointer',
                            font_weight = 'bold',
                            ),
                rx.table.cell(item.difficulty),        
    )




def problems_table() -> rx.Component:

    return rx.flex(
                rx.flex(
                    rx.input(placeholder = "Search..", 
                            value = '', 
                            on_change = QueryProblems.set_query,
                    ),
                    rx.button("Search", 
                            on_click = QueryProblems.get_problem_by_word,
                            
                        ),
                    justify = "center",
                    spacing = "2",
                    margin = "0.5rem",
                ),
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell('Title'),
                            rx.table.column_header_cell('Difficulty'),
                        ),
                    ),
                    rx.table.body(
                        rx.foreach(QueryProblems.problems, problems_list),
    
                    ),
                    variant = 'surface',
                ),
            
                direction = "column",
                spacing = "2",
                width = '80%',
)