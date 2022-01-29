"""
This module exports the BaseScreenModel class which is the superclass for data
model classes.

The model implements the observer pattern. This means that the class must
support adding, removing, and alerting observers. In this case, the model is
completely independent of controllers and views. It is important that all
registered observers implement a specific method that will be called by the
model when they are notified (in this case, it is the `model_is_changed`
method). For this, observers must be descendants of an abstract class,
inheriting which, the `model_is_changed` method must be overridden.

class BaseScreenView -- the superclass for model classes
"""


class BaseScreenModel:
    """
    The class that implements a base class for data model classes.

    Attributes
    ----------

    :attr _observers: The list of observers.
    :type _observers: list
    """

    _observers = []

    def add_observer(self, observer) -> None:
        """
        Add the instance of a view class as an observer to the list of the
        observers.

        :param observer: The instance of a view class.
        :type observer: e.g. :class:`~View.HomeTab.home_tab.HomeTabView`.
        """
        self._observers.append(observer)

    def remove_observer(self, observer) -> None:
        """
        Remove the instance of a view class as an observer from the list of the
        observers.

        :param observer: The instance of a view class.
        :type observer: e.g. :class:`~View.HomeTab.home_tab.HomeTabView`.
        """
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        """
        Notify all the observers about the model changes.

        """

        for observer in self._observers:
            observer.model_is_changed()
