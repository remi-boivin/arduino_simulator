# -*- coding: utf-8 -*-
# component.py
# Created on: January 18, 2024
# Author(s): remi-boivin

from .implementations.component_impl import ComponentImpl


class Component(ComponentImpl):
    """Facade class for electronic components.

    This class provides a simplified interface for electronic components.
    It extends the ComponentImpl class for implementation details.
    """

    def __init__(self) -> None:
        """Initialize the Component class."""
        super().__init__()
