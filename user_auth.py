from fastapi import FastAPI, Request, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
def login(username: str = Form(...), password: str = Form(...)):
    if username == "Aman" and password == "pass123":
        return {'access_token': 'fake-token-for-user', 'token_type': 'bearer'}
    raise HTTPException(status_code=400, detail="Invalid credentials")




def get_current_user(token: str = Depends(oauth_scheme)):
    return {'username': 'Aman'} 


@app.get("/profile")
def get_profile():
    pass