from typing import List
from fastapi import APIRouter,Depends, status
from sqlalchemy.orm import Session
from database import get_db
import schemas
from repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post('/')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/list', status_code=status.HTTP_200_OK, response_model = List[schemas.ShowUser])
def get_user_list(db: Session = Depends(get_db)):
    return user.user_list(db)

@router.get('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model= schemas.ShowUser)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return user.get_user_by_id(id,db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    return user.delete_user