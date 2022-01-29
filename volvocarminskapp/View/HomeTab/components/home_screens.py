"""
This module exports the screen dictionary containing the objects of the
models and controllers of the screens of the home tab.

Attributes
----------

screens: dict: The dictionary with the objects of the models and
    controllers of the screens of the home tab.
"""

from volvocarminskapp.Model.HomeTab.home_main_screen \
    import HomeMainScreenModel

from volvocarminskapp.Controller.HomeTab.home_main_screen \
    import HomeMainScreenController

screens = {
    "home_main": {
        "model": HomeMainScreenModel,
        "controller": HomeMainScreenController,
    },
}
