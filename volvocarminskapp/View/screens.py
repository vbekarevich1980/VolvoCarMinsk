# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from volvocarminskapp.Model.home_screen import HomeScreenModel
from volvocarminskapp.Model.shop_screen import ShopScreenModel
from volvocarminskapp.Model.car_screen import CarScreenModel
from volvocarminskapp.Model.contact_screen import ContactScreenModel
from volvocarminskapp.Model.account_screen import AccountScreenModel

from volvocarminskapp.Controller.home_screen import HomeScreenController
from volvocarminskapp.Controller.shop_screen import ShopScreenController
from volvocarminskapp.Controller.car_screen import CarScreenController
from volvocarminskapp.Controller.contact_screen import ContactScreenController
from volvocarminskapp.Controller.account_screen import AccountScreenController

screens = {
    "home": {
        "model": HomeScreenModel,
        "controller": HomeScreenController,
    },
    "shop": {
        "model": ShopScreenModel,
        "controller": ShopScreenController,
    },
    "car": {
        "model": CarScreenModel,
        "controller": CarScreenController,
    },
    "contact": {
        "model": ContactScreenModel,
        "controller": ContactScreenController,
    },
    "account": {
        "model": AccountScreenModel,
        "controller": AccountScreenController,
    },
}
