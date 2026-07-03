from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    case_id: Mapped[int] = mapped_column(
        ForeignKey("cases.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(String(255))

    due_date: Mapped[datetime] = mapped_column(DateTime())

    completed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )
