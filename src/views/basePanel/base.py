from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel

from src.utils.constants import BASE_PATH

Builder.load_file(str(BASE_PATH / "src" / "views" / "basePanel" / "base.kv"))


class BaseGridLayout(GridLayout):
    home_item = ObjectProperty()
    add_reminder_item = ObjectProperty()
    list_reminder_item = ObjectProperty()
    time_tracker_item = ObjectProperty()

    def activate_item(self, chosen_item):
        # De-active the other items
        for item in (
            self.home_item,
            self.add_reminder_item,
            self.list_reminder_item,
            self.time_tracker_item,
        ):
            if item == chosen_item:
                continue
            item_source_list = item.image_source.split("_")  # home_active.png
            if "active.png" in item_source_list:
                item.image_source = item_source_list[0] + ".png"
                break
        # activate the chosen item
        chosen_item.image_source = (
            chosen_item.image_source.split(".")[0] + "_active.png"
        )  # home.png


class BasePanel(TabbedPanel):
    pass
