import reflex as rx
from sqlmodel import Field, SQLModel, create_engine, table
from datetime import datetime, UTC
import bcrypt

def get_current_datetime():
    return datetime.now(UTC)

class UserBase(rx.Model):

    user_name: str =Field(index=True)
    email: str =Field(index=True)
    created_at: datetime = Field(default_factory=get_current_datetime, nullable=False)

class User(UserBase, table=True):

    id: int | None = Field(default=None, primary_key=True)
    password_hash: str = Field()

class TestCaseBase(rx.Model):

    input_case: str
    expected_output: str
    problem_id: int | None = Field(default=None, foreign_key= "problem.id")

class TestCase(TestCaseBase, table=True):

    id: int | None = Field(default=None, primary_key=True)

class ProblemBase(rx.Model):

    title: str =Field(index=True)
    description: str
    example: str
    input_description: str
    output_description: str
    difficulty: str =Field(index=True)
    user_id: int | None = Field(default=None, foreign_key= "user.id")

class Problem(ProblemBase, table=True):

    id: int | None = Field(default=None, primary_key=True)


class ProblemCreate(ProblemBase):

    pass



# YOUR_PASSWORD = os.getenv("DB_Password")

# DATABASE_URL = f"postgresql://postgres.sdqseckrdxpmcsehxgbl:{YOUR_PASSWORD}@aws-0-us-east-1.pooler.supabase.com:5432/postgres"

# connect_args = {"check_same_thread": False}
# engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)

# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)

# if __name__ == "__main__":
#     create_db_and_tables()