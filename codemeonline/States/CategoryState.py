import reflex as rx
from sqlmodel import select
from ..SqlModels.models import Category

class CategoryState(rx.State):

    categories: list[str]
    names: list[str]

    #get all the categories
    def get_categories(self):
        with rx.session() as session:
            self.categories = session.exec(select(Category)).all()
            self.names = [name.name for name in self.categories]
