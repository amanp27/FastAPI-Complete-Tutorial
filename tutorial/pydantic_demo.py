from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.get("/name", response_model=User)
def get_user():
    return User(name='Aman', age=30)