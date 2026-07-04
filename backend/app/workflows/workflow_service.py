from datetime import UTC, datetime

from app.analytics.case_analytics import CaseAnalytics
from app.automation.reminder_service import ReminderService
from app.workflows.schemas.dashboard_response import (
    DashboardResponse,
)


class WorkflowService:

    @staticmethod
    def dashboard(db) -> DashboardResponse:

        analytics = CaseAnalytics.metrics(db)

        upcoming = ReminderService.upcoming_hearings(db)

        pending = ReminderService.pending_tasks(db)

        return DashboardResponse(
            analytics=analytics,
            upcoming_hearings=len(upcoming),
            pending_tasks=len(pending),
            generated_at=datetime.now(UTC),
        )
