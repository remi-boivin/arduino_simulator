# -*- coding: utf-8 -*-
# output.py
# Created on: January 18, 2024
# Author(s): remi-boivin

from .implementations.output_impl import OutputImpl


class OutputGeneration(OutputImpl):
    """Facade class for output generation.

    The OutputGeneration class is a facade that extends the OutputImpl class to
    provide additional features or behaviors specific to generating output.

    Attributes:
        Inherits attributes from the OutputImpl class.

    Methods:
        __init__: Initializes the OutputGeneration instance.

    Usage Example:
        output_generator = OutputGeneration()
    """

    def __init__(self) -> None:
        """Initialize the OutputGeneration instance.

        This method sets up the necessary components for generating output.

        Args:
            No specific arguments for this method.

        Returns:
            None
        """
        super().__init__()
