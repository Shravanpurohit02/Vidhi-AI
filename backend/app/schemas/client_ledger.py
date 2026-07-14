from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ClientLedgerResponse(BaseModel):
    id: int
    client_id: int
    invoice_id: int | None = None
    payment_id: int | None = None
    entry_type: str
    debit: Decimal
    credit: Decimal
    remarks: str | None = None
    entry_date: datetime

    model_config = ConfigDict(from_attributes=True)
