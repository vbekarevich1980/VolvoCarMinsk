from typing import NoReturn

from volvocarminskapp.View.ContactScreen.contact_screen import \
    ContactScreenView


class ContactScreenController:
    """
    The `ContactScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.contact_screen.ContactScreenModel
        self.view = ContactScreenView(controller=self, model=self.model)

    def on_tap_button_login(self) -> NoReturn:
        """Called when the `LOGIN` button is pressed."""

    def set_user_data(self, key, value) -> NoReturn:
        """Called every time the user enters text into the text fields."""

    def get_view(self) -> ContactScreenView:
        return self.view
