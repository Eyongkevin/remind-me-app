from kivy.graphics import Rectangle
from kivy.properties import StringProperty
from kivy.uix.widget import Widget


class ItemHeaderImageWidget(Widget):
    image_source = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.after:
            self.rect_instruction = Rectangle(
                source=self.image_source, pos=self.pos, size=self.size
            )
        self.bind(
            pos=self.update_rect, size=self.update_rect, image_source=self.update_rect
        )

    def update_rect(self, *args):
        self.rect_instruction.pos = self.pos
        self.rect_instruction.size = self.size
        self.rect_instruction.source = self.image_source
