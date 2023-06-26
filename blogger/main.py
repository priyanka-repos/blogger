from fastapi import FastAPI,status,HTTPException
from sqlalchemy.orm import Session
from . import models,schemas
from .database import engine,Session

app = FastAPI()

models.Base.metadata.create_all(engine)

 
@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog):
    new_blog = models.Blogs(title=request.title, body=request.body)
    with Session() as session:
        session.add(new_blog)
        session.commit()
        return new_blog

@app.get("/blog")
def get_all():
    with Session() as session:
        blogs = session.query(models.Blogs).all()
        return blogs
    
@app.get("/blog/{id}")
def show(id):
    with Session() as session:
        blog = session.query(models.Blogs).filter(models.Blogs.id == id).first()
        if not blog:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the {id} is not found")
        return blog
    