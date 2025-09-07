from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel

from src.utils.constants import BASE_PATH

Builder.load_file(str(BASE_PATH / "src" / "views" / "basePanel" / "base.kv"))


class BaseGridLayout(GridLayout):
    pass
