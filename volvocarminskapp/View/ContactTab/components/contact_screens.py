"""
This module exports the screen dictionary containing the objects of the
models and controllers of the screens of the contact tab.

Attributes
----------

screens: dict: The dictionary with the objects of the models and
    controllers of the screens of the contact tab.
"""

from volvocarminskapp.Model.ContactTab.contact_main_screen \
    import ContactMainScreenModel

from volvocarminskapp.Controller.ContactTab.contact_main_screen \
    import ContactMainScreenController

screens = {
    "contact_main": {
        "model": ContactMainScreenModel,
        "controller": ContactMainScreenController,
    },
}
