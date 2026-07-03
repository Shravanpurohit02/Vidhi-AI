from pydantic import BaseModel, ConfigDict


class CaseCreate(BaseModel):
    title: str
    description: str = ""
    court: str = ""
    case_number: str


class CaseUpdate(BaseModel):
    title: str
    description: str
    court: str
    status: str


class CaseResponse(BaseModel):
    id: int
    owner_id: int
    title: str
    description: str
    court: str
    case_number: str
    status: str

    model_config = ConfigDict(from_attributes=True)
