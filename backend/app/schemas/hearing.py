from datetime import datetime

from pydantic import BaseModel


class HearingCreate(BaseModel):
    case_id: int
    title: str
    court: str
    hearing_date: datetime


class HearingResponse(HearingCreate):
    id: int
    status: str

    model_config = {"from_attributes": True}
