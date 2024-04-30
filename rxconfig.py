import reflex as rx
import os 
from dotenv import load_dotenv
load_dotenv()

YOUR_PASSWORD = os.getenv("DB_Password")

DATABASE_URL = f"postgresql://postgres.sdqseckrdxpmcsehxgbl:{YOUR_PASSWORD}@aws-0-us-east-1.pooler.supabase.com:5432/postgres"


config = rx.Config(
    app_name="codemeonline",
    db_url=DATABASE_URL,

)