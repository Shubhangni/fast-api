import models
from database import get_db
from sqlalchemy.orm  import Session
from fastapi import Depends,HTTPException
import models, schemas


def get_all_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, content=request.content, author=request.author, views=request.views,published=request.published, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        return blog
    else:
        raise HTTPException(status_code=404, detail="Blog not found")
    
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
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
    
def delete_blog(id: int , db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        db.delete(blog)
        db.commit()
        return {"detail": "Blog deleted"}
    else:
        raise HTTPException(status_code=404, detail="Blog not found")
