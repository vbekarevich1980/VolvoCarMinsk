from typing import NoReturn
import importlib

#from View.MainScreen.main_screen import MainScreenView
import View.MainScreen.main_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.MainScreen.main_screen)


class MainScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """



    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = View.MainScreen.main_screen.MainScreenView(controller=self, model=self.model)

    def on_tap_button_login(self) -> NoReturn:
        """Called when the `LOGIN` button is pressed."""

    def set_user_data(self, key, value) -> NoReturn:
        """Called every time the user enters text into the text fields."""

    def get_view(self) -> View.MainScreen.main_screen.MainScreenView:
        return self.view

    def on_navi_button_pressed(self, tab_to_activate):
        tab_to_inactivate = self.view.ids['navi'].previous_tab.name
        self.view.ids['navi'].switch_tab(tab_to_activate)
        self.view.ids[f'{tab_to_activate}_button'].source = f'assets/icons/{tab_to_activate}-active.png'
        self.view.manager_screens.current = tab_to_activate
        self.view.ids[f'{tab_to_inactivate}_button'].source = f'assets/icons/{tab_to_inactivate}-inactive.png'
