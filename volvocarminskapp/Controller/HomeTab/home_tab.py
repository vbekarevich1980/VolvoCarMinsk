from typing import NoReturn

from volvocarminskapp.View.HomeTab.home_tab import HomeTabView
from volvocarminskapp.View.HomeTab.components.home_screens import screens

class HomeTabController:
    """
    The `HomeTabController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """



    def __init__(self, model):
        self.model = model  # Model.home_screen.HomeTabModel
        self.view = HomeTabView(controller=self, model=self.model, screens=screens)

    def on_tap_button_login(self) -> NoReturn:
        """Called when the `LOGIN` button is pressed."""

    def set_user_data(self, key, value) -> NoReturn:
        """Called every time the user enters text into the text fields."""

    def get_view(self) -> HomeTabView:
        return self.view
