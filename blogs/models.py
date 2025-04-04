from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

# Define your models here
class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    author = Column(String(255))
    content = Column(String(1000))
    views = Column(Integer, default=0)
    published = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    email = Column(String(255), unique=True)
    is_active = Column(Boolean, default=True)
    blogs = relationship("Blog", back_populates="creator")

