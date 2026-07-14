from pydantic import BaseModel, ConfigDict


class InvoiceItemCreate(BaseModel):
    description: str
    quantity: float
    unit_price: float


class InvoiceItemUpdate(BaseModel):
    description: str | None = None
    quantity: float | None = None
    unit_price: float | None = None


class InvoiceItemResponse(BaseModel):
    id: int
    invoice_id: int
    description: str
    quantity: float
    unit_price: float

    model_config = ConfigDict(from_attributes=True)
