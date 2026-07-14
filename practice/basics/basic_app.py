from fastapi import FastAPI, APIRouter

router = APIRouter(prefix="/api/v1", tags=["GET"])


@router.get("/")
def index():
    return {"messages": "Hello FASTAPI"}


app = FastAPI()
app.include_router(router)


# from fastapi import FastAPI

# app = FastAPI()

# @app.get('/')
# def index():
#     return {"messages": "Welecome to FastAPI tutorial!"}
