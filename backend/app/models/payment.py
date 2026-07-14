from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    invoice_id: Mapped[int] = mapped_column(
        ForeignKey("invoices.id", ondelete="CASCADE"),
        index=True,
    )

    payment_date: Mapped[datetime] = mapped_column(
        DateTime(),
        default=datetime.utcnow,
    )

    amount: Mapped[float] = mapped_column(
        Numeric(12, 2),
    )

    payment_method: Mapped[str] = mapped_column(
        String(50),
    )

    reference_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="Completed",
    )

    invoice = relationship(
        "Invoice",
        back_populates="payments",
    )
