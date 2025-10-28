"""Helper functions

Provides helper functions to the entier application backend.
"""

from kivy.core.text import LabelBase

from src.utils.constants import BASE_PATH


def load_fonts():
    font_path = BASE_PATH / "assets" / "fonts" / "Roboto"

    LabelBase.register(
        name="Roboto",
        fn_regular=str(font_path / "Roboto-Thin.ttf"),
        fn_bold=str(font_path / "Roboto-Bold.ttf"),
        fn_italic=str(font_path / "Roboto-Italic.ttf"),
    )


def format_alert_time(value: str):
    """Format alert time

    Make sure all single values are formated to double character values.

    Param
    -----
    value (str): hours or minutes or seconds. Could come as single value
                `0`, `5`, `9` or double character `04`, `12`.
    Return
    ------
    value (str): formated(double character values) hours, minutes or seconds.
                for example; `4` -> `04`, `13` -> `13`
    """

    if len(value) == 0:  # ''
        return "00"
    if len(value) == 1:  # 4
        return f"0{value}"  # 04
    return value
