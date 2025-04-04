from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from schemas import Blog, ShowBlog, User, ShowUser
from database import get_db,engine
from sqlalchemy.orm import Session
import models
from hashing import Hash
from routers import blog
app = FastAPI()


models.Base.metadata.create_all(bind=engine)


@app.post('/blog', tags=['blogs'])
def create_blog(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, content=request.content, author=request.author, views=request.views,published=request.published, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

app.include_router(blog.router)
# @app.get('/blog_list', status_code=status.HTTP_200_OK, response_model=List[ShowBlog],tags=['blogs'] )
# def get_blog_list(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog,tags=['blogs'])
def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        return blog
    else:
        raise HTTPException(status_code=404, detail="Blog not found")
    

@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])
def update_blog(id: int, request: Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        blog.title = request.title
        blog.content = request.content
        blog.author = request.author
        
        blog.views = request.views
        blog.published = request.published
        db.commit()
        db.refresh(blog)
        return blog
    else:
        raise HTTPException(status_code=404, detail="Blog not found")
    

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        db.delete(blog)
        db.commit()
        return {"detail": "Blog deleted"}
    else:
        raise HTTPException(status_code=404, detail="Blog not found")


@app.post('/user',tags=['users'])
def create_user(request: User, db: Session = Depends(get_db)):
    new_user = models.User(username=request.username, password=Hash.bcrypt_password(request.password),email=request.email, is_active=request.is_active)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user_list', status_code=status.HTTP_200_OK, response_model = List[ShowUser],tags=['users'])
def get_user_list(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.get('/user/{id}', status_code=status.HTTP_202_ACCEPTED, response_model= ShowUser,tags=['users'])
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete('/user/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=['users'])
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"detail": "User deleted"}
    else:
        raise HTTPException(status_code=404, detail="User not found")