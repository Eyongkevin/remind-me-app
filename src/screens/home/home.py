from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from src import settings


class HomeScreen(Screen):
    Builder.load_file(str(settings.BASE_PATH / "src" / "screens" / "home" / "home.kv"))
