from fastapi import HTTPException, status
from app.schemas.users import UserCreate

def create_user(user: UserCreate):
    if user.age < 18:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user must be at least 18 years old"
        )
    return user