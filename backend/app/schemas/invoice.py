from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


from app.constants.invoice_status import InvoiceStatus


class InvoiceCreate(BaseModel):
    client_id: int
    issue_date: datetime
    due_date: datetime
    subtotal: Decimal = Decimal("0.00")
    tax_amount: Decimal = Decimal("0.00")
    discount_amount: Decimal = Decimal("0.00")
    total_amount: Decimal = Decimal("0.00")
    amount_paid: Decimal = Decimal("0.00")
    balance_due: Decimal = Decimal("0.00")
    status: str = InvoiceStatus.DRAFT
    notes: str | None = None


class InvoiceUpdate(BaseModel):
    issue_date: datetime | None = None
    due_date: datetime | None = None
    subtotal: Decimal | None = None
    tax_amount: Decimal | None = None
    discount_amount: Decimal | None = None
    total_amount: Decimal | None = None
    status: str | None = None
    notes: str | None = None


class InvoiceResponse(InvoiceCreate):
    id: int
    invoice_number: str
    amount_paid: Decimal

    model_config = ConfigDict(from_attributes=True)
