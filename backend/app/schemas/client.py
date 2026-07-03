from pydantic import BaseModel


class ClientCreate(BaseModel):
    full_name: str
    email: str
    phone: str
    address: str


class ClientResponse(ClientCreate):
    id: int

    model_config = {"from_attributes": True}
