import os

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanelItem

from src.utils.constants import BASE_PATH
from src.widgets.item_header_image import ItemHeaderImageWidget

Builder.load_file(
    str(BASE_PATH / "src" / "views" / "addReminderItem" / "add_reminder.kv")
)


STORE = JsonStore(str(BASE_PATH / "stores" / "file_picker_last_folder.json"))


class AddReminderItem(TabbedPanelItem, ItemHeaderImageWidget):
    label_input: ObjectProperty
    label_input_count: ObjectProperty
    selected_days: ObjectProperty
    popup_alarm_check: ObjectProperty
    sound_alarm_check: ObjectProperty
    time_hours: ObjectProperty
    time_minutes: ObjectProperty
    time_seconds: ObjectProperty
    submit: ObjectProperty

    def reset(self):

        self.label_input.text = ""
        self.time_hours.text = ""
        self.time_minutes.text = ""
        self.time_seconds.text = ""
        self.popup_alarm_check.active = False
        self.sound_alarm_check.active = True
        self.selected_days.text = ""
        DaysPopup.chosen_days = []
        SelectedSoundLabel.instance.text = "No Sound Selected"

    def try_enable_submit(self):
        if (
            len(self.label_input.text) > 2
            and self.selected_days.text
            and self.time_hours.text
            and any([self.popup_alarm_check.active, self.sound_alarm_check.active])
        ):
            self.submit.disabled = False
        else:
            self.submit.disabled = True

    def verify_time_value(self, obj, time_limit=59):
        # it is greater than 0
        if len(obj.text):
            try:
                # limit is 2 characters
                if len(obj.text) > 2:
                    raise ValueError
                # if it is numeric and respects the limit
                if int(obj.text) > time_limit:
                    raise ValueError
            except ValueError:
                obj.text = obj.text[:-1]

    def handle_label_input(self):
        label_count_format = "-{}"
        len_remaining = 27 - len(self.label_input.text)
        if len_remaining < 0:
            self.label_input.text = self.label_input.text[:-1]
        else:
            if len_remaining < 5:
                label_count_format = (
                    f"[color=#b55a5aff]{'-' if len_remaining else ''}" + "{}[/color]"
                )
            self.label_input_count.text = label_count_format.format(len_remaining)


class DaysPopup(Popup):
    chosen_days: list[str] = []

    def days_popup_check(self, is_active: bool, value: str):
        if is_active:
            DaysPopup.chosen_days.append(value)
        else:
            DaysPopup.chosen_days.remove(value)
        self._set_days_label()

    def restore_days_check(self, value: str):
        return value in DaysPopup.chosen_days

    def _set_days_label(self):
        DaysLabel.instance.text = ",".join(DaysPopup.chosen_days)


class FilePickerPopup(Popup):
    file_chooser: ObjectProperty

    def get_last_path(self):
        return (
            STORE.get("folder")["path"]
            if STORE.exists("folder")
            else os.path.expanduser("~")
        )

    def select_file(self):
        if self.file_chooser.selection:
            selected_audio = self.file_chooser.selection[0]
            SelectedSoundLabel.instance.text = self._prepare_file_name(selected_audio)
            STORE.put("folder", path=self.file_chooser.path)
        self.dismiss()

    def _prepare_file_name(self, file_path):
        DOT_LENTH = 3
        CHAR_LENTH_TO_ADD_AFTER_DOT = 2
        FILE_NAME_LENGTH_LIMIT = 18

        file_name, _, ext = file_path.split("/")[-1].rpartition(".")
        file_name_len_at_limit = len(file_name) - FILE_NAME_LENGTH_LIMIT
        if file_name_len_at_limit > 0:
            len_to_remove = (
                file_name_len_at_limit + DOT_LENTH + CHAR_LENTH_TO_ADD_AFTER_DOT
                if file_name_len_at_limit <= DOT_LENTH
                else file_name_len_at_limit
            )
            file_name = (
                file_name[: len(file_name) - len_to_remove]
                + "..."
                + file_name[-CHAR_LENTH_TO_ADD_AFTER_DOT::]
            )

        file_name = file_name + "." + ext

        return f"[color=#b55a5aff]{file_name}[/color]"


class DaysLabel(Label):
    instance = None

    def on_kv_post(self, base_widget):
        DaysLabel.instance = self
        return super().on_kv_post(base_widget)


class SelectedSoundLabel(Label):
    instance = None

    def on_kv_post(self, base_widget):
        SelectedSoundLabel.instance = self
        return super().on_kv_post(base_widget)
