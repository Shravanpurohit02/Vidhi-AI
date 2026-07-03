from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return UserService.create_user(
            db=db,
            full_name=user.full_name,
            email=user.email,
            password=user.password,
        )
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc))
