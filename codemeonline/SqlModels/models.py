import reflex as rx
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, UTC
from decimal import Decimal


def get_current_datetime():
    return datetime.now(UTC)

class User(rx.Model, table=True):

    id: int | None = Field(default=None, primary_key=True)
    user_name: str =Field(index=True)
    password_hash: str 
    email: str =Field(index=True)
    created_at: datetime = Field(default_factory=get_current_datetime, nullable=False)

class ProblemCategoryLink(rx.Model, table = True):
    problem_id: int | None = Field(default=None, foreign_key="problem.id", primary_key=True)
    category_id: int | None = Field(default=None, foreign_key="category.id", primary_key=True)

##the model to create the problems
class Problem(rx.Model, table=True):

    id: int | None = Field(default=None, primary_key=True)
    title: str =Field(index=True)
    description: str
    difficulty: str =Field(index=True)
    user_id: int | None = Field(default=None, foreign_key= "user.id")
    created_at: datetime 
    categories: list["Category"] = Relationship(back_populates="problems", link_model=ProblemCategoryLink)
    

##the model which the code its going to be compared against 
class TestCase(rx.Model, table=True):

    id: int | None = Field(default=None, primary_key=True)
    input_data: str
    expected_output: str
    problem_id: int | None = Field(default=None, index=True, foreign_key= "problem.id")

class Submission(rx.Model, table=True):
    
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, index=True, foreign_key= "user.id")
    problem_id: int | None = Field(default=None, index=True, foreign_key= "problem.id")
    source_code :str
    submission_time: Decimal | None = Field(default=None)
    created_at: datetime 

#here is where the results will be stored
class Result(rx.Model, table=True):

    id: int | None = Field(default=None, primary_key=True)
    submission_id: int | None = Field(default=None, index=True, foreign_key= "submission.id")
    testcase_id: int | None = Field(default=None, index=True, foreign_key= "testcase.id")
    passed: bool
    execution_time: Decimal | None = Field(default=None)
    memory_usage: Decimal | None = Field(default=None)
    created_at: datetime 

class Category(rx.Model, table=True):

    id: int | None = Field(default=None, primary_key=True)
    name:str = Field(index=True)
    description:str | None = Field(default=None)
    problems: list["Problem"] = Relationship(back_populates="categories", link_model=ProblemCategoryLink)