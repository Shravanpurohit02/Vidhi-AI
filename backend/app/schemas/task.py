from datetime import datetime

from pydantic import BaseModel


class TaskCreate(BaseModel):
    case_id: int
    title: str
    due_date: datetime


class TaskResponse(TaskCreate):
    id: int
    completed: bool

    model_config = {"from_attributes": True}
