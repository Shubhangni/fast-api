from pydantic import BaseModel
from typing import List, Optional

class Blog(BaseModel):
    title: str
    content: str
    author: str
    views: int = 0
    published: Optional[bool] = False


class User(BaseModel):
    username: str
    password: str
    email: str
    is_active: Optional[bool] = True

class ShowUser(BaseModel):
    username:str
    email:str
    blogs : List[Blog]
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    content: str
    author: str
    creator: ShowUser
    class Config():
        orm_mode = True



