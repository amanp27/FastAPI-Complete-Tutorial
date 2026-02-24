from pydantic import BaseModel, Field
from typing import Optional, List

class Employee(BaseModel):
    id: int = Field(..., gt=0, description="The unique identifier for the employee")
    name: str = Field(..., min_length=1, max_length=30, description="The name of the employee")
    dep: str = Field(..., description="The department of the employee")
    age: Optional[int] = Field(None, gt=0, description="The age of the employee")