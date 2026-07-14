from enum import StrEnum


class InvoiceStatus(StrEnum):
    DRAFT = "Draft"
    ISSUED = "Issued"
    PARTIALLY_PAID = "Partially Paid"
    PAID = "Paid"
    OVERDUE = "Overdue"
    CANCELLED = "Cancelled"
