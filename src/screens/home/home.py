from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from src import settings


class HomeScreen(BoxLayout, Screen):
    Builder.load_file(str(settings.BASE_PATH / "src" / "screens" / "home" / "home.kv"))
