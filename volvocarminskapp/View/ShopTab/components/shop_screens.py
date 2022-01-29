"""
This module exports the screen dictionary containing the objects of the
models and controllers of the screens of the shop tab.

Attributes
----------

screens: dict: The dictionary with the objects of the models and
    controllers of the screens of the shop tab.
"""

from volvocarminskapp.Model.ShopTab.shop_main_screen \
    import ShopMainScreenModel
from volvocarminskapp.Model.ShopTab.new_cars_locator_screen \
    import NewCarsLocatorScreenModel
from volvocarminskapp.Model.ShopTab.used_cars_locator_screen \
    import UsedCarsLocatorScreenModel

from volvocarminskapp.Controller.ShopTab.shop_main_screen \
    import ShopMainScreenController
from volvocarminskapp.Controller.ShopTab.new_cars_locator_screen \
    import NewCarsLocatorScreenController
from volvocarminskapp.Controller.ShopTab.used_cars_locator_screen \
    import UsedCarsLocatorScreenController


screens = {
    "shop_main": {
        "model": ShopMainScreenModel,
        "controller": ShopMainScreenController,
    },
    "new_cars_locator": {
        "model": NewCarsLocatorScreenModel,
        "controller": NewCarsLocatorScreenController,
    },
    "used_cars_locator": {
        "model": UsedCarsLocatorScreenModel,
        "controller": UsedCarsLocatorScreenController,
    },
}
