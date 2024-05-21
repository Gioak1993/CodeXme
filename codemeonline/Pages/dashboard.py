import reflex as rx 
from sqlmodel import select
from ..States.Auth import AuthState
from ..SqlModels.models import User, Problem

class Dashboard(rx.State):

    problems: list[Problem]
    email:str

            
    async def dashboard(self):
        
        cookie = await self.get_state(AuthState)
        user_id = cookie.user_id_cookie

        with rx.session() as session:
            user = session.exec(select(User).where(User.id == user_id)).one()
            self.email = user.email
            self.problems = session.exec(select(Problem).where(Problem.user_id == user_id)).all()

def dashboard() -> rx.Component:

    return rx.vstack(
        rx.text(f'Hello {Dashboard.email}'),
        rx.data_editor(
            columns=['Title', 'Difficulty'],
            data= Dashboard.problems,
        ),
)

