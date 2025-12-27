from fastapi import APIRouter, status,  Depends, Query, HTTPException
from app.schemas.users import UserCreate, UserResponce
from app.services.users_service import create_user, get_users, get_users_by_name,update_user,delete_user
from app.db.database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "",
    response_model=UserResponce,
    status_code=status.HTTP_201_CREATED
)
def create_user_route(user:UserCreate,db:Session=Depends(get_db)):
    return create_user(db,user)

@router.get(
    "",
    response_model=List[UserResponce]
)

def list_user(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
   return get_users(db,skip=skip, limit=limit)

@router.get(
    "/search",
    response_model=List[UserResponce]
)

def search_users(
    name: str,
    db: Session = Depends(get_db)
):
    users = get_users_by_name(db,name)
    
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found"
        )
       
       
    return users
   
@router.put(
    "/{user_id}",
    response_model=UserResponce
)
def update_user_route(
    user_id: int,
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return update_user(db,user_id,user)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK
)
def delete_user_route(
    user_id: int,
    db: Session = Depends(get_db)
):
    return delete_user(db,user_id)
