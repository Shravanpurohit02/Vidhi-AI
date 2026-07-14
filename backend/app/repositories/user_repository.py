from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    @staticmethod
    def get_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def create(
        db: Session,
        full_name: str,
        email: str,
        password: str,
        role: str = "lawyer",
    ):
        user = User(
            full_name=full_name,
            email=email,
            hashed_password=password,
            role=role,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
