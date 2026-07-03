from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository


class UserService:

    @staticmethod
    def create_user(db: Session, full_name: str, email: str, password: str):

        existing = UserRepository.get_by_email(db, email)

        if existing:
            raise ValueError("Email already exists")

        return UserRepository.create(
            db=db,
            full_name=full_name,
            email=email,
            password=password,
        )
