"""
The entry point to the application.

The application uses the MVC template.
"""

from kivy.config import Config

Config.set('graphics', 'width', '330')
Config.set('graphics', 'height', '650')

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from typing import NoReturn, Any

from kivymd.app import MDApp

from View.navigation_tabs import navigation_tabs


class VolvoCarMinskApp(MDApp):
    """
    The app main class.

    Attributes
    ----------
    :attr main_screen: The instance of the root screen of the application.
    :type main_screen: :class:`~kivy.uix.screenmanager.Screen`

    :attr navigation: The instance of the bottom navigation of the application.
    :type navigation: :class:`~kivymd.uix.bottomnavigation.MDBottomNavigation`
    """

    def __init__(self, **kwargs: [str, Any]) -> None:
        """
        Construct an instance of VolvoCarMinskApp class and set main_screen
        and navigation instances.

        :param kwargs: Any key parameters to be passed.
        """
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        self.main_screen = Builder.load_file('View/main_screen.kv')
        self.navigation = self.main_screen.ids.navi

    def build(self) -> Screen:
        """
        Initialize the application and returns the root widget - a screen;
        it is called only once.

        :return: The root widget.
        """
        self.theme_cls.primary_palette = "Amber"  # TODO Set the theme
        self.generate_navigation_tabs()

        return self.main_screen

    def generate_navigation_tabs(self) -> NoReturn:
        """
        Create and add tabs (screens) to the bottom navigation of the
        application.

        If a tab needs to be added, it is done by adding a new tab to the
        `View.navigation_tabs.py` module.
        """

        for i, name_tab in enumerate(navigation_tabs.keys()):
            model = navigation_tabs[name_tab]["model"]()
            controller = navigation_tabs[name_tab]["controller"](model)
            view = controller.get_view()
            view.navigation = self.navigation
            view.name = name_tab
            self.navigation.add_widget(view)


VolvoCarMinskApp().run()
