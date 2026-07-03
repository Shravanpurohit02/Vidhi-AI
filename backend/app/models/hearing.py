from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Hearing(Base):
    __tablename__ = "hearings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    case_id: Mapped[int] = mapped_column(
        ForeignKey("cases.id"),
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(String(255))

    court: Mapped[str] = mapped_column(String(255))

    hearing_date: Mapped[datetime] = mapped_column(DateTime())

    status: Mapped[str] = mapped_column(
        String(50),
        default="Scheduled",
    )
