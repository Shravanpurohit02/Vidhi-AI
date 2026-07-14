from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class ClientLedger(Base):
    __tablename__ = "client_ledger"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    client_id: Mapped[int] = mapped_column(
        ForeignKey("clients.id", ondelete="CASCADE"),
        index=True,
    )

    invoice_id: Mapped[int | None] = mapped_column(
        ForeignKey("invoices.id", ondelete="SET NULL"),
        nullable=True,
    )

    payment_id: Mapped[int | None] = mapped_column(
        ForeignKey("payments.id", ondelete="SET NULL"),
        nullable=True,
    )

    entry_date: Mapped[datetime] = mapped_column(
        DateTime(),
        default=datetime.utcnow,
    )

    entry_type: Mapped[str] = mapped_column(
        String(30),
    )

    debit: Mapped[float] = mapped_column(
        Numeric(12, 2),
        default=0,
    )

    credit: Mapped[float] = mapped_column(
        Numeric(12, 2),
        default=0,
    )

    balance: Mapped[float] = mapped_column(
        Numeric(12, 2),
        default=0,
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )
