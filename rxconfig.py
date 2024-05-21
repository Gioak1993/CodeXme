import reflex as rx
import os 
from dotenv import load_dotenv
load_dotenv()

DB_URL = os.getenv("DB_URL")


config = rx.Config(
    app_name="codemeonline",
    db_url=DB_URL,
    api_url="http://codexme.up.railway.app:8000"
)