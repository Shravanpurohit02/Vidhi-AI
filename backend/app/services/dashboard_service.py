from sqlalchemy import func

from app.models.case import Case
from app.models.client import Client
from app.models.document import Document
from app.models.hearing import Hearing
from app.models.task import Task


class DashboardService:

    @staticmethod
    def summary(db):

        return {
            "cases": db.query(func.count(Case.id)).scalar(),
            "documents": db.query(func.count(Document.id)).scalar(),
            "clients": db.query(func.count(Client.id)).scalar(),
            "hearings": db.query(func.count(Hearing.id)).scalar(),
            "tasks": db.query(func.count(Task.id)).scalar(),
        }
