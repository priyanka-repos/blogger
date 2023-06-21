from fastapi import FastAPI
from . import schemas,models
from  .database import SessionLocal,engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine) 

@app.post('/blog')
def create(request: schemas.Blog):
    return request
