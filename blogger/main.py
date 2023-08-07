from fastapi import FastAPI,status,HTTPException

from blogger.router.blog import blogRouter
from blogger.router.user import userRouter
from blogger.router.authentication import router


app = FastAPI()
app.include_router(blogRouter)
app.include_router(userRouter)
app.include_router(router)







