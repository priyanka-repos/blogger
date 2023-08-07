from fastapi import APIRouter,status,HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import models,schemas
from ..database import engine,Session
from ..hashing import Hash

blogRouter = APIRouter(
    tags=['blogs'],
    prefix='/blog'
)

models.Base.metadata.create_all(engine)

session = Session()

@blogRouter.post('/create', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog):
    new_blog = models.Blogs(title=request.title, body=request.body, user_id = 1)
    session.add(new_blog)
    session.commit()
    return new_blog

@blogRouter.get("/get",response_model=List[schemas.ShowBlog])
def get_all():
    blogs = session.query(models.Blogs).all()
    return blogs

@blogRouter.get("/{id}",status_code=200,response_model=schemas.ShowBlog)
def show(id):
    blog = session.query(models.Blogs).filter(models.Blogs.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the {id} is not found")
    return blog

