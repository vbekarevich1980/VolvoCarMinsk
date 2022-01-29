"""
This module exports UsedCarsLocatorScreenView class presenting the screen for
used car locator tool.

class UsedCarsLocatorScreenView -- the class for the screen for used car
                locator tool, inherits from BaseScreenView
"""

from typing import NoReturn

from volvocarminskapp.View.base_screen import BaseScreenView


class UsedCarsLocatorScreenView(BaseScreenView):
    """
    The class that implements the screen for used car locator tool.

    """

    def model_is_changed(self) -> NoReturn:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.

        """
