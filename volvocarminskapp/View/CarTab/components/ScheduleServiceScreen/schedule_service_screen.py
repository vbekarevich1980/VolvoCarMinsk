"""
This module exports ScheduleServiceScreenView class presenting the screen for
schedule service tool.

class ScheduleServiceScreenView -- the class for the screen for schedule
                                service tool, inherits from BaseScreenView
"""

from typing import NoReturn

from volvocarminskapp.View.base_screen import BaseScreenView


class ScheduleServiceScreenView(BaseScreenView):
    """
    The class that implements the screen for schedule service tool.

    """

    def model_is_changed(self) -> NoReturn:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.

        """
