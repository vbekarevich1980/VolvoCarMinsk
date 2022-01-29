"""
This module exports HomeTabView class presenting the tab for home screens
of the application.

class HomeTabView -- the class for the tab for home screens of the
                 application, inherits from BaseTabView
"""

from typing import NoReturn

from volvocarminskapp.View.base_tab import BaseTabView


class HomeTabView(BaseTabView):
    """
    The class that implements the tab for home screens of the application.

    """

    def model_is_changed(self) -> NoReturn:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.

        """
