from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanelItem

from src.utils.constants import BASE_PATH
from src.widgets.item_header_image import ItemHeaderImageWidget

Builder.load_file(str(BASE_PATH / "src" / "views" / "homeItem" / "home.kv"))


class HomeItem(TabbedPanelItem, ItemHeaderImageWidget):
    pass
