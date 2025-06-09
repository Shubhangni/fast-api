
from fastapi import APIRouter,Depends, status
from sqlalchemy.orm import Session
from typing import List
import schemas
from database import get_db
from repository import blog
from routers import Oauth

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

@router.get('/list', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog] )
def get_blog_list(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(Oauth.get_current_user)):
    return blog.get_all_blog(db)

@router.post('/')
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create_blog(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    return blog.get_blog_by_id(id, db)
    

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update_blog(id, request, db)
    

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    return blog.delete_blog(id, db)

