"""
This module exports HomeMainScreenView class presenting the main screen for
the home tab of the application.

class HomeMainScreenView -- the class for the main screen for the home tab
                        of the application, inherits from BaseScreenView
"""

from typing import NoReturn

from volvocarminskapp.View.base_screen import BaseScreenView


class HomeMainScreenView(BaseScreenView):
    """
    The class that implements the main screen for the home tab of the
    application.

    """

    def model_is_changed(self) -> NoReturn:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.

        """
