from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class LitigationTimeline(Base):
    __tablename__ = "litigation_timelines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[int] = mapped_column(
        ForeignKey("cases.id"),
        index=True,
    )
    event: Mapped[str] = mapped_column(String(255))
    event_time: Mapped[datetime] = mapped_column(DateTime())
