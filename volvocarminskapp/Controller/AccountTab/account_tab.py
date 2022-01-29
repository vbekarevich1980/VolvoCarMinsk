from typing import NoReturn

from volvocarminskapp.View.AccountTab.account_tab import \
    AccountTabView
from volvocarminskapp.View.AccountTab.components.account_screens import screens


class AccountTabController:
    """
    The `AccountTabController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.account_screen.AccountTabModel
        self.view = AccountTabView(controller=self, model=self.model, screens=screens)

    def on_tap_button_login(self) -> NoReturn:
        """Called when the `LOGIN` button is pressed."""

    def set_user_data(self, key, value) -> NoReturn:
        """Called every time the user enters text into the text fields."""

    def get_view(self) -> AccountTabView:
        return self.view
