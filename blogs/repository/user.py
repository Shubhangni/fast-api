import models, schemas
from hashing import Hash
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException


def create_user(request: schemas.User, db : Session = Depends(get_db)):
    new_user = models.User(username=request.username, password=Hash.bcrypt_password(request.password),email=request.email, is_active=request.is_active)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def user_list(db : Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

def get_user_by_id(id:int, db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

def delete_user(id:int, db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"detail": "User deleted"}
    else:
        raise HTTPException(status_code=404, detail="User not found")