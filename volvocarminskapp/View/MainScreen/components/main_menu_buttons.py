from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDIconButton, MDRectangleFlatIconButton

from volvocarminskapp.View.NewCarsLocatorScreen.new_cars_locator_screen import \
    NewCarsLocatorScreenView
from volvocarminskapp.View.ShopScreen.shop_screen import ShopScreenView


class ShopTab(ScreenManager):
    def __init__(self, **kwargs):
        super(ShopTab, self).__init__(**kwargs)
        self.add_widget(ShopScreenView(name='menu'))
        self.add_widget(NewCarsLocatorScreenView(name='new_cars_locator'))


class VCMIconButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class VCMRectangleFlatIconButton(MDIconButton, MDRectangleFlatIconButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)