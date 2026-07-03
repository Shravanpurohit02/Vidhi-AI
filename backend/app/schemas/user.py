from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
