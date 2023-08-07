from fastapi import APIRouter,HTTPException,status
from ..schemas import Login
from ..models import User
from ..database import Session
from ..hashing import Hash
router = APIRouter(
    tags=['Login']
)

session = Session()
@router.post("/login")
def login(request:Login):
    user = session.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with this email is not found")
    else:
        if not Hash.verify(user.password,request.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Password")

    return user