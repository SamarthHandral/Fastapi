from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel 
from pydantic import EmailStr

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/search")
def search_item(q:str,number:int = 100):
    return {"query":q,"number":number}

@app.get("/poo/{name}")
def search_items(name:str, limit: int = 10):
    return {"query": name, "limit": limit}


class UserCreate(BaseModel):
    name: str
    email : EmailStr
    age : int

@app.post("/users")
def create_user(user: UserCreate):
    return {
        "message": "user created sucessfully",
        "user": user
    }
    