from fastapi import HTTPException, status
from app.schemas.users import UserCreate
from app.db.models import User
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_user(db: Session , user: UserCreate):
    db_user = User(
        name= user.name,
        email= user.email,
        age= user.age
    )
    try :
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    except IntegrityError :
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists"
        )