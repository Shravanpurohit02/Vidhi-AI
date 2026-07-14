from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    invoice_id: Mapped[int] = mapped_column(
        ForeignKey("invoices.id", ondelete="CASCADE"),
        index=True,
    )

    description: Mapped[str] = mapped_column(String(255))

    quantity: Mapped[float] = mapped_column(
        Numeric(10, 2),
        default=1,
    )

    unit_price: Mapped[float] = mapped_column(
        Numeric(12, 2),
        default=0,
    )

    amount: Mapped[float] = mapped_column(
        Numeric(12, 2),
        default=0,
    )

    invoice = relationship(
        "Invoice",
        back_populates="items",
    )
