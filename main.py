from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

from src.utils.helper import load_fonts
from src.views.basePanel.base import BaseGridLayout


class MainApp(MDApp):
    def build(self):
        Window.size = (300, 500)
        return BaseGridLayout()


if __name__ == "__main__":
    Window.clearcolor = get_color_from_hex("#5B5959")
    load_fonts()
    MainApp().run()
