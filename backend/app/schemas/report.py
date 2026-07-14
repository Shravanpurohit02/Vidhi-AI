from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class InvoiceReportResponse(BaseModel):
    id: int
    invoice_number: str
    client_id: int
    issue_date: datetime
    due_date: datetime
    total_amount: Decimal
    amount_paid: Decimal
    balance_due: Decimal
    status: str

    model_config = ConfigDict(from_attributes=True)
