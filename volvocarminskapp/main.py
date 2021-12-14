from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class VolvoCarMinskApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, World", halign="center")


VolvoCarMinskApp().run()
