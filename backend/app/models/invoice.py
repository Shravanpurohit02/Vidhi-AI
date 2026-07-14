from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


from app.constants.invoice_status import InvoiceStatus


class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    invoice_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True,
    )

    client_id: Mapped[int] = mapped_column(
        ForeignKey("clients.id"),
        index=True,
    )

    issue_date: Mapped[datetime] = mapped_column(DateTime())

    due_date: Mapped[datetime] = mapped_column(DateTime())

    status: Mapped[str] = mapped_column(
        String(30),
        default=InvoiceStatus.DRAFT,
    )

    subtotal: Mapped[float] = mapped_column(
        Numeric(12, 2),
        default=0,
    )

    tax_amount: Mapped[float] = mapped_column(
        Numeric(12, 2),
        default=0,
    )

    discount_amount: Mapped[float] = mapped_column(
        Numeric(12, 2),
        default=0,
    )

    total_amount: Mapped[float] = mapped_column(
        Numeric(12, 2),
        default=0,
    )

    amount_paid: Mapped[float] = mapped_column(
        Numeric(12, 2),
        default=0,
    )

    balance_due: Mapped[float] = mapped_column(
        Numeric(12, 2),
        default=0,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(),
        default=datetime.utcnow,
    )

    items = relationship(
        "InvoiceItem",
        cascade="all, delete-orphan",
        back_populates="invoice",
    )

    payments = relationship(
        "Payment",
        cascade="all, delete-orphan",
        back_populates="invoice",
    )
