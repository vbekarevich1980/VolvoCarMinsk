"""
This module exports the Observer class which is the abstract superclass for
view classes.

class Observer -- the abstract superclass exporting model_is_changed method
                to be called when the model changes
"""


class Observer:
    """
    The abstract superclass for all observers.

    """

    def model_is_changed(self):
        """
        The method that will be called on the observer when the model changes.

        """
