from sqlalchemy import func

from app.models.case import Case
from app.models.document import Document
from app.models.hearing import Hearing
from app.models.task import Task


class CaseAnalytics:

    @staticmethod
    def metrics(db):

        return {
            "total_cases": db.query(func.count(Case.id)).scalar(),
            "total_documents": db.query(func.count(Document.id)).scalar(),
            "total_hearings": db.query(func.count(Hearing.id)).scalar(),
            "total_tasks": db.query(func.count(Task.id)).scalar(),
        }
