from datetime import datetime

from pydantic import BaseModel


class DashboardResponse(BaseModel):
    analytics: dict

    upcoming_hearings: int

    pending_tasks: int

    generated_at: datetime
