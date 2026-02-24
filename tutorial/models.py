from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    dep: str
    age: int