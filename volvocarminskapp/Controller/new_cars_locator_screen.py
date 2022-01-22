from typing import NoReturn
import importlib

#from View.ShopScreen.components.NewCarsLocatorScreen.new_cars_locator_screen\
#    import \
#    NewCarsLocatorScreenView
import View.NewCarsLocatorScreen.new_cars_locator_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.NewCarsLocatorScreen.new_cars_locator_screen)

class NewCarsLocatorScreenController:
    """
    The `NewCarsLocatorScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.new_cars_locator_screen.NewCarsLocatorScreenModel
        self.view = View.NewCarsLocatorScreen.new_cars_locator_screen.NewCarsLocatorScreenView(controller=self, model=self.model)

    def on_tap_button_login(self) -> NoReturn:
        """Called when the `LOGIN` button is pressed."""

    def set_user_data(self, key, value) -> NoReturn:
        """Called every time the user enters text into the text fields."""

    def get_view(self) -> View.NewCarsLocatorScreen.new_cars_locator_screen.NewCarsLocatorScreenView:
        return self.view
