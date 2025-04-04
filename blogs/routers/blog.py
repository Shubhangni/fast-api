from fastapi import APIRouter
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends, status
from models import Blog
from schemas import ShowBlog
from database import get_db

router = APIRouter()

@router.get('/blog_list', status_code=status.HTTP_200_OK, response_model=List[ShowBlog],tags=['blogs'] )
def get_blog_list(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs