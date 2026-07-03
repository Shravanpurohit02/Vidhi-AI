from sqlalchemy.orm import Session

from app.repositories.workspace_repository import WorkspaceRepository


class WorkspaceService:

    @staticmethod
    def create_hearing(db: Session, data: dict):
        return WorkspaceRepository.create_hearing(db, data)

    @staticmethod
    def create_task(db: Session, data: dict):
        return WorkspaceRepository.create_task(db, data)

    @staticmethod
    def hearings(db: Session):
        return WorkspaceRepository.list_hearings(db)

    @staticmethod
    def tasks(db: Session):
        return WorkspaceRepository.list_tasks(db)
