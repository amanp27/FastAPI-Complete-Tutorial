"""
Defining the Pydantic models for data validation for CRUD application.
"""

from pydantic import BaseModel, EmailStr

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr


class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id: int

    class Config:
        orm_mode = True # This allows Pydantic to work with SQLAlchemy models, enabling seamless data validation when interacting with the database.