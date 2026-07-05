from pydantic import BaseModel, ConfigDict


class ClientCreate(BaseModel):
    full_name: str
    email: str
    phone: str
    address: str


class ClientResponse(ClientCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
