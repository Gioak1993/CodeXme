"""Base state. Schema is inspired by https://drawsql.app/templates/twitter."""
from typing import Optional

import reflex as rx
from codemeonline.SqlModels.models import User
from .ClientStorage import ClientStorage

class Log(rx.State):
    """The logged state for the app."""

    user: Optional[User] = None

    # def logout(self):
    #     """Log out a user."""
    #     if ClientStorage.user_id == "2":
    #         print(ClientStorage.user_id)
    #     rx.remove_cookie("user_id")
    #     print(ClientStorage.user_id)
    #     return rx.redirect("/")

    # def check_login(self):
    #     """Check if a user is logged in."""
    #     if not self.logged_in:
    #         return rx.redirect("/login")
    
    # @rx.var
    # def logged_in(self):
    #     """Check if a user is logged in."""
    #     return ClientStorage.user_id != ""
    
    