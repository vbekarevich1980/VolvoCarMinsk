# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from volvocarminskapp.Model.main_screen import MainScreenModel
from volvocarminskapp.Model.shop_screen import ShopScreenModel
from volvocarminskapp.Model.new_cars_locator_screen import NewCarsLocatorScreenModel


from volvocarminskapp.Controller.main_screen import MainScreenController
from volvocarminskapp.Controller.shop_screen import ShopScreenController
from volvocarminskapp.Controller.new_cars_locator_screen import NewCarsLocatorScreenController

screens = {
    "home": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
    "shop": {
        "model": ShopScreenModel,
        "controller": ShopScreenController,
    },
    "new_cars_locator": {
        "model": NewCarsLocatorScreenModel,
        "controller": NewCarsLocatorScreenController,
    },
}
