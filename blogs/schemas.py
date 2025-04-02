from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title: str
    content: str
    author: str
    views: int = 0
    published: Optional[bool] = False

class ShowBlog(BaseModel):
    title: str
    content: str
    author: str
    class Config():
        orm_mode = True

class User(BaseModel):
    username: str
    password: str
    email: str
    is_active: Optional[bool] = True

class ShowUser(BaseModel):
    username:str
    email:str

    class Config():
        orm_mode = True