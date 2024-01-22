# -*- coding: utf-8 -*-
# execution.py
# Created on: January 18, 2024
# Author(s): remi-boivin

from .implementations.execution_impl import ExecutionImpl


class Execution(ExecutionImpl):
    """Facade class for execution handling.

    The Execution class serves as a facade, extending the ExecutionImpl class
    to provide additional features or behaviors related to execution in the
    application.

    Attributes:
        Inherits attributes from the ExecutionImpl class.

    Methods:
        __init__: Initializes the Execution instance.

    Usage Example:
        execution_handler = Execution(name="example", properties={"key": "value"}) # noqa E501
    """

    def __init__(self, name: str, properties: dict) -> None:
        """Initialize the Execution instance.

        This method extends the initialization process to handle execution in a
        way specific to the application.

        Args:
            name (str): The name of the execution.
            properties (dict): Properties specific to the execution.

        Returns:
            None
        """
        super().__init__()
