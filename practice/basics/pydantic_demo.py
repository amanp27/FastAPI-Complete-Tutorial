from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

router = APIRouter(prefix="/user/v1", tags=['GET'])

@router.get('/user', response_model=User)
def get_user_details():
    return User(id=1, name='Aman')

app = FastAPI()
app.include_router(router)


# @app.get("/user", response_model=User)
# def get_user():
#     return User(id=69, name='chinmayee')