"""Base state. Schema is inspired by https://drawsql.app/templates/twitter."""
from typing import Optional

import reflex as rx
from codemeonline.SqlModels.models import User


class Log(rx.State):
    """The logged state for the app."""

    user: Optional[User] = None

    
    