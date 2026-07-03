from datetime import UTC, datetime

from app.models.hearing import Hearing
from app.models.task import Task


class ReminderService:

    @staticmethod
    def upcoming_hearings(db):

        now = datetime.now(UTC)

        return (
            db.query(Hearing)
            .filter(Hearing.hearing_date >= now)
            .order_by(Hearing.hearing_date)
            .all()
        )

    @staticmethod
    def pending_tasks(db):

        return (
            db.query(Task)
            .filter(Task.completed.is_(False))
            .order_by(Task.due_date)
            .all()
        )
