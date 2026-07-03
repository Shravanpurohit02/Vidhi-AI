from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class CourtSchedule(Base):
    __tablename__ = "court_schedules"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    court: Mapped[str] = mapped_column(String(255))
    event: Mapped[str] = mapped_column(String(255))
    starts_at: Mapped[datetime] = mapped_column(DateTime())
    ends_at: Mapped[datetime] = mapped_column(DateTime())
