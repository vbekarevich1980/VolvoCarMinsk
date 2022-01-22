# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.main_screen import MainScreenModel
from Model.shop_screen import ShopScreenModel
from Model.new_cars_locator_screen import NewCarsLocatorScreenModel


from Controller.main_screen import MainScreenController
from Controller.shop_screen import ShopScreenController
from Controller.new_cars_locator_screen import NewCarsLocatorScreenController

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
