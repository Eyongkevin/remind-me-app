from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivymd.uix.button import MDIconButton
from kivymd.uix.menu import MDDropdownMenu

from src.services import remindme as reminder_service
from src.utils.constants import BASE_PATH
from src.widgets.item_header_image import ItemHeaderImageWidget

Builder.load_file(
    str(BASE_PATH / "src" / "views" / "listReminderItem" / "list_reminder.kv")
)


class ListReminderItem(TabbedPanelItem, ItemHeaderImageWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_reminder: int | None = None
        self.menu_items = [
            {
                "viewclass": "MDIconButton",
                "icon": "pencil",
                "on_release": lambda x="edit": self.menu_callaback(x),
            },
            {
                "viewclass": "MDIconButton",
                "icon": "delete",
                "on_release": lambda x="delete": self.menu_callaback(x),
            },
            {
                "viewclass": "MDIconButton",
                "icon": "state-machine",
                "on_release": lambda x="state": self.menu_callaback(x),
            },
        ]
        self.dropdown = MDDropdownMenu(
            items=self.menu_items, position="auto", border_margin="8dp"
        )

    def menu_callaback(self, option: str):
        """Handle menu option for selected item"""
        print(f"Selected: {option} on {self.selected_reminder}")

    def open_menu(self, button: MDIconButton, reminder_id: int):
        """Open dropdown menu attached to the three-dots icon"""
        self.dropdown.caller = button
        self.selected_reminder = reminder_id
        self.dropdown.open()


class ReminderListView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = reminder_service.fetch_data()


class ReminderState(RecycleDataViewBehavior, BoxLayout):
    id = NumericProperty()
    label = StringProperty()
    alert_time = StringProperty()
    days = StringProperty()
    state = StringProperty()
    status = StringProperty()
    repeat = StringProperty()
    alert_types = StringProperty()


class ReminderListFilterPopup(Popup):
    days: list[str] = []
    status: list[str] = []
    state: list[str] = []
    alert_types: list[str] = []
    repeat: list[str] = []

    @classmethod
    def reset(cls):
        cls.days = []
        cls.status = []
        cls.state = []
        cls.alert_types = []
        cls.repeat = []

    def dismiss(self, *_args, **kwargs):
        super().dismiss(*_args, **kwargs)
        if not any([self.days, self.status, self.state, self.alert_types, self.repeat]):
            remove_filter()
            return
        self.create_filter_option_display()

    def filter_check(self, is_active: bool, value: str, option: str):
        if is_active:
            ReminderListFilterPopup.__dict__[option].append(value)
        else:
            ReminderListFilterPopup.__dict__[option].remove(value)

    def restore_filter_check(self, value: str, option: str):
        return value in ReminderListFilterPopup.__dict__[option]

    def create_filter_option_display(self):
        remove_filter()
        filter_widget = FilterGridLayout()
        size = 0
        for options in [
            ("Days", self.days),
            ("Status", self.status),
            ("State", self.state),
            ("alert", self.alert_types),
            ("repeat", self.repeat),
        ]:
            if options[1]:
                print(options)
                size += 15
                grid = GridLayout(cols=2, padding=(15, 15))
                grid.add_widget(
                    Label(text=options[0], font_size="10dp", size_hint_x=0.1)
                )
                grid.add_widget(
                    Label(
                        text=", ".join(options[1]),
                        font_size="8dp",
                        size_hint_x=0.9,
                        halign="left",
                    )
                )
                filter_widget.filter_options.add_widget(grid)

        filter_widget.height = f"{size}dp"

        app = App.get_running_app()
        app.root.list_reminder_item.reminder_list_box.add_widget(filter_widget, index=1)


class FilterGridLayout(GridLayout):
    def clear_filters(self):
        ReminderListFilterPopup.reset()
        remove_filter()


def remove_filter():
    app = App.get_running_app()
    if len(app.root.list_reminder_item.reminder_list_box.children) > 1:
        app.root.list_reminder_item.reminder_list_box.remove_widget(
            app.root.list_reminder_item.reminder_list_box.children[1]
        )
