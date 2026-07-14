from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Branding(Base):
    __tablename__ = "branding"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    firm_name: Mapped[str] = mapped_column(String(200))
    advocate_name: Mapped[str] = mapped_column(String(200))

    address: Mapped[str] = mapped_column(String(500))
    city: Mapped[str] = mapped_column(String(100))
    state: Mapped[str] = mapped_column(String(100))
    pincode: Mapped[str] = mapped_column(String(20))

    phone: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(200))
    website: Mapped[str | None] = mapped_column(String(200), nullable=True)

    gst_number: Mapped[str | None] = mapped_column(String(30), nullable=True)
    bar_registration_no: Mapped[str | None] = mapped_column(String(50), nullable=True)

    logo_path: Mapped[str | None] = mapped_column(String(500), nullable=True)
    signature_path: Mapped[str | None] = mapped_column(String(500), nullable=True)

    primary_color: Mapped[str] = mapped_column(
        String(20),
        default="#1F4E79",
    )

    secondary_color: Mapped[str] = mapped_column(
        String(20),
        default="#404040",
    )

    default_invoice_template: Mapped[str] = mapped_column(
        String(50),
        default="classic",
    )
