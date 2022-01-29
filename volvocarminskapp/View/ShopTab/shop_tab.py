"""
This module exports ShopTabView class presenting the tab for shopping
screens of the application.

class ShopTabView -- the class for the tab for shopping screens of the
                    application, inherits from BaseTabView
"""

from typing import NoReturn

from volvocarminskapp.View.base_tab import BaseTabView


class ShopTabView(BaseTabView):
    """
    The class that implements the tab for shopping screens of the application.

    """

    def model_is_changed(self) -> NoReturn:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.

        """
