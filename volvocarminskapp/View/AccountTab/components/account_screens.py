"""
This module exports the screen dictionary containing the objects of the
models and controllers of the screens of the account tab.

Attributes
----------

screens: dict: The dictionary with the objects of the models and
    controllers of the screens of the account tab.
"""

from volvocarminskapp.Model.AccountTab.account_main_screen \
    import AccountMainScreenModel

from volvocarminskapp.Controller.AccountTab.account_main_screen \
    import AccountMainScreenController


screens = {
    "account_main": {
        "model": AccountMainScreenModel,
        "controller": AccountMainScreenController,
    },
}
