import reflex as rx
from ..SqlModels.models import Problem
from sqlmodel import select


class QueryProblems(rx.State):

    problems: list[Problem]
    query: str
    pagination: int 
    limit: int = 20
    offset: int = 0


    def get_all_problems(self):
        with rx.session() as session:
            self.problems = session.exec(select(Problem).offset(self.offset).limit(self.limit)).all()

    def get_problem_by_word(self):
        with rx.session() as session:
            self.problems = session.exec(select(Problem).where(Problem.title.contains(self.query.capitalize()))).all()
            









