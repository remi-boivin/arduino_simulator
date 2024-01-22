# -*- coding: utf-8 -*-
# simulator.py
# Created on: January 18, 2024
# Author(s): remi-boivin

from .implementations.simulator_impl import SimulatorCoreImpl


class SimulatorCore(SimulatorCoreImpl):
    """Facade class for the simulator core.

    The SimulatorCore class is a facade that extends the SimulatorCoreImpl
    class to provide additional features or behaviors specific to the
    simulator core.

    Attributes:
        Inherits attributes from the SimulatorCoreImpl class.

    Methods:
        __init__: Initializes the SimulatorCore instance.

    Usage Example:
        simulator = SimulatorCore()
    """

    def __init__(self) -> None:
        """Initialize the SimulatorCore instance.

        This method sets up the necessary components for the simulator core.

        Args:
            No specific arguments for this method.

        Returns:
            None
        """
        super().__init__()
