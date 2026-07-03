from datetime import date

from sqlalchemy import Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class CauseList(Base):
    __tablename__ = "cause_lists"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    court: Mapped[str] = mapped_column(String(255))
    bench: Mapped[str] = mapped_column(String(255))
    cause_date: Mapped[date] = mapped_column(Date)
    item_number: Mapped[int] = mapped_column(Integer)
    case_number: Mapped[str] = mapped_column(String(255))
    title: Mapped[str] = mapped_column(String(500))
