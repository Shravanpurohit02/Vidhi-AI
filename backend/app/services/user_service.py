from sqlalchemy.orm import Session

from app.auth.password import hash_password
from app.repositories.user_repository import UserRepository


class UserService:

    @staticmethod
    def create_user(db: Session, full_name: str, email: str, password: str):

        existing = UserRepository.get_by_email(db, email)

        if existing:
            raise ValueError("Email already exists")

        hashed_password = hash_password(password)

        return UserRepository.create(
            db=db,
            full_name=full_name,
            email=email,
            password=hashed_password,
        )
