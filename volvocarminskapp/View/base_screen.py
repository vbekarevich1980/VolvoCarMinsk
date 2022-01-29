"""
This module exports the BaseScreenView class which is the superclass for
view classes implementing visual representation of the application data model.

class BaseScreenView -- the parent class for view classes implementing visual
                        representation of the application data model,
                        inherits from ThemableBehavior, MDScreen and Observer
"""
from typing import Any

from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen

from volvocarminskapp.Utility.observer import Observer


class BaseScreenView(ThemableBehavior, MDScreen, Observer):
    """
    The base class that implements a visual representation of the application
    data model. The view classes of the application tab screens must be
    inherited from this class.

    Attributes
    ----------

    :attr app: The application object.
    :type app: :class:`~kivymd.app.MDApp`

    :attr controller: A controller object - e.g.
        :class:`~Controller.HomeTab.home_main_screen.HomeMainScreenController`.
    :type controller: :class:`~kivy.properties.ObjectProperty`
        and defaults to `None`

    :attr model: A model object -
        e.g. :class:`~Model.HomeTab.home_main_screen.HomeMainScreenModel`.
    :type model: :class:`~kivy.properties.ObjectProperty`
        and defaults to `None`

    :attr manager_screens: A screen manager object -
        :class:`~kivy.uix.screenmanager.ScreenManager`.
    :type manager_screens: :class:`~kivy.properties.ObjectProperty`
        and defaults to `None`
    """

    controller = ObjectProperty()

    model = ObjectProperty()

    manager_screens = ObjectProperty()

    def __init__(self, **kwargs: [str, Any]) -> None:
        """
        Construct an instance of BaseScreenView class and set app, model,
        manager_screens attributes.

        :param kwargs: Any key parameters to be passed.
        """
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        # Adding a view class as observer.
        self.model.add_observer(self)
