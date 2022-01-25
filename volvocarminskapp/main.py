
"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""

from kivy.config import Config


Config.set('graphics', 'width', '330')
Config.set('graphics', 'height', '650')

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
#from volvocarminskapp.View.MainScreen.main_screen import MainScreen



from typing import NoReturn

from kivymd.app import MDApp

from View.screens import screens


class VolvoCarMinskApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.main_screen = Builder.load_file('View/MainScreen/main_screen.kv')
        self.manager_screens = self.main_screen.ids.navi

    def build(self) -> Screen:
        """
        Initializes the application; it will be called only once.
        If this method returns a widget (tree), it will be used as the root
        widget and added to the window.

        :return:
            None or a root :class:`~kivy.uix.widget.Widget` instance
            if no self.root exists.
        """

        self.theme_cls.primary_palette = "Amber"
        self.generate_application_screens()
        return self.main_screen

    def generate_application_screens(self) -> NoReturn:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """

        for i, name_screen in enumerate(screens.keys()):

            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)


VolvoCarMinskApp().run()
