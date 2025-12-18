from fastapi import APIRouter, status
from app.schemas.users import UserCreate, UserResponce
from app.services.users_service import create_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "",
    response_model=UserResponce,
    status_code=status.HTTP_201_CREATED
)
def create_user_route(user:UserCreate):
    return create_user(user)