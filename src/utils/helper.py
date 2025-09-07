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
