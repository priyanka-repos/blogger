from sqlalchemy import Column, Integer, String,ForeignKey
from .database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Blogs(Base):
    __tablename__ = 'blogs'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    body: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]

    blogs = relationship("Blogs",back_populates="creator")
