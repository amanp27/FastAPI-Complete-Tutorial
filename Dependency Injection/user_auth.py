from fastapi import FastAPI, Request, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordBearer
from starlette import status

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
def login(username: str = Form(...), password: str = Form(...)):
    if username == "Aman" and password == "pass123":
        return {'access_token': 'valid_token', 'token_type': 'bearer'}
    raise HTTPException(status_code=400, detail="Invalid credentials")

def decode_token(token: str):
    if token == 'valid_token':
        return {"username": "Aman"}
    raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, 
                        detail="Invalid Authentication Credentials")


def get_current_user(oauth2_token: str = Depends(oauth2_scheme)):
    return decode_token(oauth2_token)


@app.get("/profile")
def get_profile(user=Depends(get_current_user)):
    return {"user": user["username"], "message": "This is the profile page. You are authenticated."}
