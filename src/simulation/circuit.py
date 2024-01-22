# -*- coding: utf-8 -*-
# circuit.py
# Created on: January 18, 2024
# Author(s): remi-boivin

from .implementations.circuit_impl import CircuitImpl


class Circuit(CircuitImpl):
    """Facade class for circuit management.

    The Circuit class is a facade that extends the CircuitImpl class to provide
    additional features or behaviors specific to managing the circuit in the
    application.

    Attributes:
        Inherits attributes from the CircuitImpl class.

    Methods:
        __init__: Initializes the Circuit instance.

    Usage Example:
        circuit_manager = Circuit()
    """

    def __init__(self) -> None:
        """Initialize the Circuit instance.

        This method sets up the necessary components for managing the circuit.

        Args:
            No specific arguments for this method.

        Returns:
            None
        """
        super().__init__()
