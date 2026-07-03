from app.analytics.case_analytics import CaseAnalytics
from app.automation.reminder_service import ReminderService


class WorkflowService:

    @staticmethod
    def dashboard(db):

        return {
            "analytics": CaseAnalytics.metrics(db),
            "upcoming_hearings": len(
                ReminderService.upcoming_hearings(db)
            ),
            "pending_tasks": len(
                ReminderService.pending_tasks(db)
            ),
        }
