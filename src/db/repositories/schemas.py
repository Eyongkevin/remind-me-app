"""Schema

Pydantic data models, validations and serializers
"""

from datetime import datetime, time

from pydantic import BaseModel, ConfigDict, Json


class RemindMeBase(BaseModel):
    """
    base model
    """

    label: str
    days: str
    repeat: bool
    alert_time: time
    alert_sound: str


class CreateRemindMe(RemindMeBase):
    """
    Data model for creating reminder event
    """

    alert_type: str


class ReadRemindMe(RemindMeBase):
    """
    Data model for reading reminder event.

    New in pydantic 2.x
    Allow Pydantic to read the fields directly from the SQLAlchemy

    Old version
    ---
    class config:
        orm_mode = True

    New version
    ---
    model_config = ConfigDict(from_attributes=True)
    """

    id: int
    days: Json[list[str]]
    alert_type: Json[dict[str, bool]]
    active: bool
    created_at: datetime
    modified_at: datetime

    model_config = ConfigDict(from_attributes=True)
