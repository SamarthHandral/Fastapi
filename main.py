from typing import Union

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel,  EmailStr

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

class UserResponce(BaseModel):
    name:str
    email : EmailStr


@app.post(
    "/users",
    response_model=UserResponce,
    status_code=status.HTTP_201_CREATED
    )
def create_user(user: UserCreate):
    if user.age < 18:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user must be at least 18 years old"
        )
    return user
    