import reflex as rx 
from ..Pages.newproblem import CreateProblem
from ..States.CategoryState import CategoryState


class DynamicInputState(rx.State):
    
    categories_list: list[str] = ['']
    #add a field when the user wants to add more than one category



    def add_field(self):
        self.categories_list.append(' ')
    
    def delete_field(self):
        if len(self.categories_list) >= 1:
            del self.categories_list[-1]
        else:
            pass


def dropdown_category() -> rx.Component:
    return rx.vstack(
                rx.foreach(DynamicInputState.categories_list, dropdown2),
                rx.hstack(
                rx.button("Add", on_click=DynamicInputState.add_field),
                rx.button("Delete", on_click=[DynamicInputState.delete_field, CreateProblem.del_category], color_scheme='red'),),
                align='center',
    )

def dropdown2(item) -> rx.Component:
    return rx.select( CategoryState.names, placeholder='Select a category',on_change=CreateProblem.add_category)








# def dropdown_category_selection(categories_list:list[str]) -> rx.Component:

#         return rx.select.root(
#                         rx.select.trigger(placeholder="Select a Category"),
#                             rx.select.content(
#                                 rx.select.group(
#                                     rx.select.label('Category'),
#                                         rx.foreach(CategoryState.names, dropdown_category_item),
#                                 ),
#                         ),
#         )

# #function made for use on foreach to choose category
# def dropdown_category_item(category_item) -> rx.Component:
#     return  rx.select.item(
#                 rx.text(category_item, on_click=CreateProblem.add_category(category_item),)
# )
