from fastapi import APIRouter, status,  Depends
from app.schemas.users import UserCreate, UserResponce
from app.services.users_service import create_user
from app.db.database import get_db
from sqlalchemy.orm import Session

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