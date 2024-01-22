# -*- coding: utf-8 -*-
# arduino.py
# Created on: January 18, 2024
# Author(s): remi-boivin

from .implementations.arduino_impl import ArduinoImpl


class ArduinoCodeExecution(ArduinoImpl):
    """Facade class for Arduino code execution.

    This class serves as a facade, extending the ArduinoImpl class to
    encapsulate code execution specific to Arduino devices.

    Attributes:
        Inherits attributes from the ArduinoImpl class.

    Methods:
        __init__: Initializes the ArduinoCodeExecution instance.

    Usage Example:
        arduino_executor = ArduinoCodeExecution()
    """

    def __init__(self) -> None:
        """Initialize the ArduinoCodeExecution instance.

        This method sets up the necessary components for
        Arduino code execution.

        Args:
            No specific arguments for this method.

        Returns:
            None
        """
        super().__init__()
