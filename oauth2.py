from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
import jwt2

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
def get_current_user(token: str = Depends(oauth2_scheme)):
    return jwt2.verify_token(token)