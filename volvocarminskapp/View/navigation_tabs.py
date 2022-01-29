"""
This module exports the screen dictionary containing the objects of the
models and controllers of the main screens (navigation tabs) of the
application.

Attributes
----------

navigation_tabs: dict: The dictionary with the objects of the models and
    controllers of the main screens (navigation tabs) of the application.
"""

from volvocarminskapp.Model.HomeTab.home_tab import HomeTabModel
from volvocarminskapp.Model.ShopTab.shop_tab import ShopTabModel
from volvocarminskapp.Model.CarTab.car_tab import CarTabModel
from volvocarminskapp.Model.ContactTab.contact_tab import ContactTabModel
from volvocarminskapp.Model.AccountTab.account_tab import AccountTabModel

from volvocarminskapp.Controller.HomeTab.home_tab import HomeTabController
from volvocarminskapp.Controller.ShopTab.shop_tab import ShopTabController
from volvocarminskapp.Controller.CarTab.car_tab import CarTabController
from volvocarminskapp.Controller.ContactTab.contact_tab \
    import ContactTabController
from volvocarminskapp.Controller.AccountTab.account_tab \
    import AccountTabController

navigation_tabs = {
    "home": {
        "model": HomeTabModel,
        "controller": HomeTabController,
    },
    "shop": {
        "model": ShopTabModel,
        "controller": ShopTabController,
    },
    "car": {
        "model": CarTabModel,
        "controller": CarTabController,
    },
    "contact": {
        "model": ContactTabModel,
        "controller": ContactTabController,
    },
    "account": {
        "model": AccountTabModel,
        "controller": AccountTabController,
    },
}
