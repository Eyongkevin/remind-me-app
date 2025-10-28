"""Model

Handle model for the remindme table.

Uses SQLAlchemy 2.x and sqlite database.

Sqlite doesn't support lists, dict and other complicated data types
- list -> str = '["Mon", "Tues"]'
- dict -> json = '{"sound": true, "popup": false}'
"""

from datetime import time

from sqlalchemy import TIME, TIMESTAMP, Boolean, String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.db.config import Model


class RemindMe(Model):
    __tablename__ = "remindme"

    id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(String(100), index=True)
    days: Mapped[str] = mapped_column(String(100))  # '["Mon", "Tue"]
    alert_sound: Mapped[str] = mapped_column(String(50))
    alert_time: Mapped[time] = mapped_column(TIME)
    alert_type: Mapped[str] = mapped_column(
        String(50)
    )  # '{"sound" true, "popup": false}'
    active: Mapped[bool] = mapped_column(Boolean, default=True, index=True)
    repeat: Mapped[bool]
    created_at: Mapped[str] = mapped_column(
        TIMESTAMP, server_default=func.current_timestamp()
    )
    modified_at: Mapped[str] = mapped_column(
        TIMESTAMP,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )

    def __repr__(self) -> str:
        return f'RemindMe({self.id}, "{self.label}")'
