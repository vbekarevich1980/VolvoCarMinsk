"""
This module exports the screen dictionary containing the objects of the
models and controllers of the screens of the car tab.

Attributes
----------

screens: dict: The dictionary with the objects of the models and
    controllers of the screens of the car tab.
"""

from volvocarminskapp.Model.CarTab.car_main_screen \
    import CarMainScreenModel
from volvocarminskapp.Model.CarTab.schedule_screen \
    import ScheduleServiceScreenModel

from volvocarminskapp.Controller.CarTab.car_main_screen \
    import CarMainScreenController
from volvocarminskapp.Controller.CarTab.schedule_service_screen \
    import ScheduleServiceScreenController

screens = {
    "car_main": {
        "model": CarMainScreenModel,
        "controller": CarMainScreenController,
    },
    "schedule_service": {
        "model": ScheduleServiceScreenModel,
        "controller": ScheduleServiceScreenController,
    },
}
