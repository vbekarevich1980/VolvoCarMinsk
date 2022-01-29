"""
This module exports MainScreenBottomNavigation, BaseTabView and
MainScreenNavigationButton classes presenting elements of the application
main navigation.

class MainScreenBottomNavigation -- the class for the application navigation,
                    inherits from MDBottomNavigation
class BaseTabView -- the class for a tab of the application bottom navigation,
                    inherits from MDBottomNavigationItem and Observer
class MainScreenNavigationButton -- the class for a custom buttons of the
                    application bottom navigation using custom icons,
                    inherits from ButtonBehavior and Image
"""

from typing import NoReturn, Any

from kivy.properties import ObjectProperty, DictProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager

from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigationItem, \
    MDBottomNavigation

from volvocarminskapp.Utility.observer import Observer


class MainScreenBottomNavigation(MDBottomNavigation):
    """
    The class that implements the application navigation.

    """

    def on_navi_button_pressed(self, tab_to_activate: str) -> None:
        """
        Switch the bottom navigation to the tab clicked on.

        :param tab_to_activate: The tab to show.
        """
        tab_to_inactivate = self.previous_tab.name
        self.switch_tab(tab_to_activate)
        self.parent.ids[
            f'{tab_to_activate}_button'
        ].source = f'assets/icons/{tab_to_activate}-active.png'
        self.parent.ids[
            f'{tab_to_inactivate}_button'
        ].source = f'assets/icons/{tab_to_inactivate}-inactive.png'


class BaseTabView(MDBottomNavigationItem, Observer):
    """
    The base class that implements a visual representation of the tabs of the
    application bottom navigation. The view class of a tab must be inherited
    from this class.

    Attributes
    ----------

    :attr app: The application object.
    :type app: :class:`~kivymd.app.MDApp`

    :attr controller: A controller object -
        e.g. :class:`~Controller.HomeTab.home_tab.HomeTabController`.
    :type controller: :class:`~kivy.properties.ObjectProperty`
        and defaults to `None`

    :attr model: A model object -
        e.g. :class:`~Model.HomeTab.home_tab.HomeTabModel`.
    :type model: :class:`~kivy.properties.ObjectProperty`
        and defaults to `None`

    :attr navigation: The navigation object -
        :class:`~kivymd.uix.bottomnavigation.MDBottomNavigation`.
    :type navigation: :class:`~kivy.properties.ObjectProperty`
        and defaults to `None`

    :attr manager_screens: A screen manager object -
        :class:`~kivy.uix.screenmanager.ScreenManager`.
    :type manager_screens: :class:`~kivy.properties.ObjectProperty`
        and defaults to `None`

    :attr screens: The dictionary with the objects of the models and
        controllers of the screens of the application navigation tab.
    :type screens: :class:`~kivy.properties.DictProperty`
        and defaults to `{}`
    """

    controller = ObjectProperty()

    model = ObjectProperty()

    navigation = ObjectProperty()

    manager_screens = ObjectProperty()

    screens = DictProperty()

    def __init__(self, **kwargs: [str, Any]) -> None:
        """
        Construct an instance of BaseTabView class and set app, model,
        manager_screens attributes.

        :param kwargs: Any key parameters to be passed.
        """
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        # Adding a view class as observer.
        self.model.add_observer(self)
        self.manager_screens = ScreenManager()
        self.generate_tab_screens()
        self.add_widget(self.manager_screens)

    def generate_tab_screens(self) -> NoReturn:
        """
        Create and add screens to the screen manger of a bottom navigation tab.

        If a screen needs to be added, it is done by adding a new screen to
        the 'screens' dictionary.
        """

        screens = self.screens

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)


class MainScreenNavigationButton(ButtonBehavior, Image):
    """
    The base class that implements a custom button for the application
    bottom navigation using custom icons.

    """
