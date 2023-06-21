from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
app = FastAPI()

class Blog(BaseModel):
    title:str
    body:str
    published_at: Optional[str]

@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    
    if published:
        return {"data": f'{limit} published blogs from the db'}
    else:
        return {"data": f'{limit} blogs from the db'}
    
@app.get("/blog/{id}/comments")
def comments(id,limit=10):
    return {"data": {'1','2'}}  

@app.post("/blog")
def createBlog(request:Blog):
    return {"data":request.title} 



if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)