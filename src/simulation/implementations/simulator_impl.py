# -*- coding: utf-8 -*-
# simulator_impl.py
# Created on: January 18, 2024
# Last updated on: January 22, 2024# Author(s): remi-boivin

from ..circuit import Circuit


class SimulatorCoreImpl:
    """Implementation class for simulator core functionality.

    This class provides a base for implementing features and behaviors related
    to the simulator core.

    Attributes:
        circuit: An instance of the Circuit class.

    Methods:
        __init__: Initializes the SimulatorCoreImpl instance.

    Usage Example:
        core_instance = SimulatorCore()
    """

    def __init__(self) -> None:
        """Initialize the SimulatorCoreImpl instance.

        This method sets up the necessary components
        for simulator core functionality.

        Args:
            No specific arguments for this method.

        Returns:
            None
        """
        self.circuit = Circuit()
