from sqlalchemy.orm import Session

from app.models.client import Client


class ClientRepository:

    @staticmethod
    def create(db: Session, data: dict):
        obj = Client(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def list(db: Session):
        return db.query(Client).all()
