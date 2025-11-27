"""Service

Provide services to the views.

This service abstract the view from the repository and specifically
provide data formatting before saving using the repository
"""

import json
from datetime import time

from src.db.repositories import remindme as repo_remindme
from src.db.repositories import schemas
from src.utils.constants import BASE_PATH
from src.utils.helper import format_alert_time


def insert(
    hours: str,
    minutes: str,
    seconds: str,
    days: list[str],
    repeat: bool,
    alert_type_popup: bool,
    alert_type_sound: bool,
    selected_sound: str,
    label: str,
):
    """
    Format reminder data to the right format before calling repository to be saved

    Param
    -------
    hours (str): reminder alert hour
    minutes (str): reminder alert minutes
    seconds (str): reminder alert seconds
    days (list[str]): list of days when the reminder event should be triggered
    repeat (bool): whether the reminder event should repeat
    alert_type_popup (bool): whether the reminder event should trigger a popup
    alert_type_sound (bool): whether the reminder event should trigger a sound
    selected_sound (str): The sound that will play when the event is triggered.
                          The sound is played only if `alert_type_sound` is set to `True`
    label (str): The label of the reminder event.
    """

    # Alert Time -> hh:mm:ss
    # 13, 4 -> 04, '' -> '00'
    alert_time: time = time.fromisoformat(
        f"{format_alert_time(hours)}:{format_alert_time(minutes)}:{format_alert_time(seconds)}"
    )

    # days -> list[str] -> json
    alert_days: str = json.dumps(days)
    alert_type: str = json.dumps({"sound": alert_type_sound, "popup": alert_type_popup})
    alert_sound: str = (
        selected_sound
        if selected_sound
        else str(BASE_PATH / "assets" / "sounds" / "sound.wav")
    )

    # Validate with Pydantic
    validated_data = schemas.CreateRemindMe(
        alert_time=alert_time,
        days=alert_days,
        repeat=repeat,
        alert_type=alert_type,
        alert_sound=alert_sound,
        label=label,
    )

    # Repository to save the reminder data
    return repo_remindme.create_remindme(validated_data)


def fetch_data() -> list[dict[str, str | int]]:
    return [
        {
            "id": 1,
            "label": "Short break",
            "alert_time": "11:30:00",  # time
            "days": "Mon, Tue, Wed, Thur, Fri, Sat",  # list[str]
            "state": "active",
            "status": "pending",
            "alert_types": "sound, popup",  # dict[str, bool]
            "repeat": "true",  # bool
        },
        {
            "id": 2,
            "label": "Done for the day",
            "alert_time": "22:00:00",
            "days": "Tue, Fri, Sun",
            "state": "inactive",
            "status": "passed",
            "alert_types": "sound",
            "repeat": "false",
        },
        {
            "id": 3,
            "label": "Review project",
            "alert_time": "13:00:00",
            "days": "Mon, Thur, Fri",
            "state": "active",
            "status": "pending",
            "alert_types": "popup",
            "repeat": "true",
        },
        {
            "id": 4,
            "label": "Family time",
            "alert_time": "15:00:00",
            "days": "Tue, Fri, Sat",
            "state": "active",
            "status": "passed",
            "alert_types": "sound",
            "repeat": "false",
        },
        {
            "id": 5,
            "label": "Take a walk",
            "alert_time": "17:30:00",
            "days": "Mon, Thur, Fri, Sat",
            "state": "active",
            "status": "pending",
            "alert_types": "sound, popup",
            "repeat": "true",
        },
        {
            "id": 6,
            "label": "Watch news",
            "alert_time": "20:00:00",
            "days": "Tue, Fri, Sat",
            "state": "active",
            "status": "passed",
            "alert_types": "popup",
            "repeat": "true",
        },
    ]
