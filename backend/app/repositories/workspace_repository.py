from sqlalchemy.orm import Session

from app.models.hearing import Hearing
from app.models.task import Task


class WorkspaceRepository:

    @staticmethod
    def create_hearing(db: Session, data: dict):
        obj = Hearing(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def create_task(db: Session, data: dict):
        obj = Task(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def list_hearings(db: Session):
        return db.query(Hearing).all()

    @staticmethod
    def list_tasks(db: Session):
        return db.query(Task).all()
