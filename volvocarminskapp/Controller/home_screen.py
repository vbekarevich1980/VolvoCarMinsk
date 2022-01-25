from typing import NoReturn

from volvocarminskapp.View.HomeScreen.home_screen import HomeScreenView


class HomeScreenController:
    """
    The `HomeScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """



    def __init__(self, model):
        self.model = model  # Model.home_screen.HomeScreenModel
        self.view = HomeScreenView(controller=self, model=self.model)

    def on_tap_button_login(self) -> NoReturn:
        """Called when the `LOGIN` button is pressed."""

    def set_user_data(self, key, value) -> NoReturn:
        """Called every time the user enters text into the text fields."""

    def get_view(self) -> HomeScreenView:
        return self.view

    def on_navi_button_pressed(self, tab_to_activate):
        tab_to_inactivate = self.view.ids['navi'].previous_tab.name
        self.view.ids['navi'].switch_tab(tab_to_activate)
        self.view.ids[f'{tab_to_activate}_button'].source = f'assets/icons/{tab_to_activate}-active.png'
        #self.view.manager_screens.current = tab_to_activate
        #self.view.manager_screens.current = 'car'
        self.view.ids[f'{tab_to_inactivate}_button'].source = f'assets/icons/{tab_to_inactivate}-inactive.png'
