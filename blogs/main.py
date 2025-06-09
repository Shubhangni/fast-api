
from fastapi import FastAPI
from database import engine
import models
from routers import blog, user, authentication

app = FastAPI()


models.Base.metadata.create_all(bind=engine)


app.include_router(blog.router)

app.include_router(user.router)

app.include_router(authentication.router)
















#### previous routes #####
# @app.post('/blog', tags=['blogs'])
# def create_blog(request: Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, content=request.content, author=request.author, views=request.views,published=request.published, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog