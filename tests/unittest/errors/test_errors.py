# -*- coding: utf-8 -*-
# errors.py
# Created on: January 18, 2024
# Author(s): remi-boivin

from .implementations.errors_impl import ErrorImpl


class ErrorHandling(ErrorImpl):
    """Extended class for handling errors in the application.

    The ErrorHandling class extends the ErrorImpl class to provide additional
    error-handling features or behaviors specific to the application's needs.

    Attributes:
        Inherits attributes from the ErrorImpl class.

    Methods:
        __init__: Initializes the ErrorHandling instance.

    Usage Example:
        error_handler = ErrorHandling()
    """

    def __init__(self) -> None:
        """Initialize the ErrorHandling instance.

        This method extends the initialization process to handle errors in a
        way specific to the application.

        Args:
            No specific arguments for this method.

        Returns:
            None
        """
        super().__init__()
