from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp

from src.screens.home.home import HomeScreen


class MainScreenManager(ScreenManager):
    pass


class RemindMeApp(MDApp):
    def build(self):
        Window.size = (500, 500)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

        sm = MainScreenManager()
        sm.add_widget(HomeScreen(name="home"))

        sm.current = "home"
        return sm


if __name__ == "__main__":
    Window.clearcolor = get_color_from_hex("#f8f1f0")
    RemindMeApp().run()
