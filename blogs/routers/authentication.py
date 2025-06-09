from fastapi import APIRouter,HTTPException,Depends, status
from datetime import timedelta
import models
from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash 
from . import JWTtoken
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/login",
    tags=['Authentication']
)

ACCESS_TOKEN_EXPIRE_MINUTES = 30

@router.post('/', status_code = status.HTTP_200_OK)
def user_login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    print("User details", user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="INVALID CREDENTIALS")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="INCORRECT PASSWORD")
    ## GENERATE JWT TOKEN
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = JWTtoken.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    print("access token ------------",access_token)
    return {'access_token':access_token, 'token_type':"bearer"}
    
