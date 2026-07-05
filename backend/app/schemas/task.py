from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TaskCreate(BaseModel):
    case_id: int
    title: str
    due_date: datetime


class TaskResponse(TaskCreate):
    id: int
    completed: bool

    model_config = ConfigDict(from_attributes=True)
