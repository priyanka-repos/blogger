from sqlalchemy import Column, Integer, String
from .database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Blogs(Base):
    __tablename__ = 'blogs'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    body: Mapped[str]