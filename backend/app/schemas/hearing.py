from datetime import datetime

from pydantic import BaseModel, ConfigDict


class HearingCreate(BaseModel):
    case_id: int
    title: str
    court: str
    hearing_date: datetime


class HearingResponse(HearingCreate):
    id: int
    status: str

    model_config = ConfigDict(from_attributes=True)
