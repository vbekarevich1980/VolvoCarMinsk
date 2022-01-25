from kivy.properties import ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigationItem, \
    MDBottomNavigation

from volvocarminskapp.Utility.observer import Observer


class MainScreen(Screen):
    pass


class MainScreenBottomNavigation(MDBottomNavigation):
    
    def __init__(self, **kwargs):
        super(MainScreenBottomNavigation, self).__init__(**kwargs)
        self.set_first_tab_on()


    def set_first_tab_on(self):
        self.current = 'home'

    def on_navi_button_pressed(self, tab_to_activate):
        print(tab_to_activate)
        print(self)
        print(self.previous_tab)
        print(self.current)
        print(self.ids)
        print(self.tabs)

        tab_to_inactivate = self.previous_tab.name
        self.switch_tab(tab_to_activate)
        self.parent.ids[
            f'{tab_to_activate}_button'].source = f'assets/icons/{tab_to_activate}-active.png'
        #self.current = tab_to_activate
        self.parent.ids[
            f'{tab_to_inactivate}_button'].source = f'assets/icons/{tab_to_inactivate}-inactive.png'


class MainScreenNavigationButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainScreenBaseView(MDBottomNavigationItem, Observer):
    """
    A base class that implements a visual representation of the model data
    :class:`~Model.home_screen.HomeScreenModel`.
    The view class must be inherited from this class.
    """

    controller = ObjectProperty()
    """
    Controller object - :class:`~Controller.home_screen.HomeScreenController`.

    :attr:`controller` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    model = ObjectProperty()
    """
    Model object - :class:`~Model.home_screen.HomeScreenModel`.

    :attr:`model` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    manager_screens = ObjectProperty()
    """
    Screen manager object - :class:`~kivymd.uix.bottomnavigation.MDBottomNavigation`.

    :attr:`manager_screens` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, **kw):
        #super(MainScreenBaseView, self).__init__(**kw)
        super().__init__(**kw)
        # Often you need to get access to the application object from the view
        # class. You can do this using this attribute.
        self.app = MDApp.get_running_app()
        # Adding a view class as observer.
        self.model.add_observer(self)
