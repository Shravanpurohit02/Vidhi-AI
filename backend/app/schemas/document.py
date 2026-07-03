from pydantic import BaseModel, ConfigDict


class DocumentCreate(BaseModel):
    case_id: int
    title: str
    filename: str
    content_type: str
    file_path: str


class DocumentResponse(BaseModel):
    id: int
    case_id: int
    title: str
    filename: str
    content_type: str
    file_path: str

    model_config = ConfigDict(from_attributes=True)
