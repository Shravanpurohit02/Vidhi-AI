from sqlalchemy.orm import Session

from app.repositories.client_repository import ClientRepository


class ClientService:

    @staticmethod
    def create(db: Session, data: dict):
        return ClientRepository.create(db, data)

    @staticmethod
    def list(db: Session):
        return ClientRepository.list(db)
