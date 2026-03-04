from fastapi import FastAPI
# from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'https://my-frontend-app.com',
        'http://localhost:3000'
    ],
    allow_credentials=True, #To allow cookies
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=['*']
)

