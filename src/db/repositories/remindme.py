"""Repository

Abstraction between the model and the views
"""

from src.db.config import SessionLocal
from src.db.models.remindme import RemindMe
from src.db.repositories import schemas


def create_remindme(
    reminder_data: schemas.CreateRemindMe,
) -> schemas.ReadRemindMe | None:
    """
    Save reminder event to the database.

    Params
    ------
    reminder_data (schema.CreateRemindMe): data about the reminder event.

    Raises
    ______
    Exception: Any exception that may occur when inserting in the database

    Returns
    -------
    reminder (schema.ReadRemindMe): Optional, saved reminder event.
    """

    try:
        db = SessionLocal()
        reminder = RemindMe(
            label=reminder_data.label,
            days=reminder_data.days,
            alert_sound=reminder_data.alert_sound,
            alert_type=reminder_data.alert_type,
            alert_time=reminder_data.alert_time,
            repeat=reminder_data.repeat,
        )
        db.add(reminder)
        db.commit()
        db.refresh(reminder)
        db.close()

        return schemas.ReadRemindMe.model_validate(reminder, strict=True)
    except Exception:
        return None
