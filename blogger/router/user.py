from fastapi import APIRouter,status,HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import models,schemas
from ..database import engine,Session
from ..hashing import Hash

userRouter = APIRouter(
    tags=['users'],
    prefix='/user'
)

models.Base.metadata.create_all(engine)

session = Session()

@userRouter.post('/')
def create_user(request:schemas.User):
    
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@userRouter.get("/",response_model=List[schemas.ShowUser])
def show_user():
    users = session.query(models.User).all()
    return users

@userRouter.get("/{id}", response_model=schemas.ShowUser)
def get_user(id):
    user = session.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the {id} is not found")
    return user
    