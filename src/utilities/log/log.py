# -*- coding: utf-8 -*-
# log.py
# Created on: January 22, 2024

import inspect
from datetime import datetime
from ..level import Level


class Log:
    """
    A logging utility class for creating log messages
    with various severity levels.

    This class provides functionality to log messages with timestamps,
    file origins, and specified severity levels.
    It supports dynamic log level setting to control the verbosity of output.

    Attributes:
        log_level (Level): The current logging level; messages with a level
                           lower than this will not be logged.

  Methods:
        __init__(self, log_level=Level.ERROR):
            Initializes the Log instance with a specified logging level.
            - log_level (Level, optional): The initial logging level.
              Defaults to Level.ERROR.

        log(self, buff, level=Level.ERROR):
            Logs a message with a given severity level if it meets or exceeds
            the current log level.

            The log message includes:
                - a timestamp
                - the name of the logging level,
                - the name of the file from which the log was called,
                  and the log message itself.

            - buff (str): The log message to output.
            - level (Level, optional): The severity level of the log message.
              Defaults to Level.ERROR.

        set_log_level(self, log_level):
            Sets the logging level of the Log instance.
            - log_level (Level): The new logging level to be set.

        get_log_level(self):
            Retrieves the current logging level of the Log instance.
            Returns:
            - Level: The current logging level.

    Usage Example:
        log = Log(log_level=Level.DEBUG)
        log.log("This is a debug message.", Level.DEBUG)
    """

    def __init__(self, log_level=Level.ERROR) -> None:
        """
        Initializes the Log instance with a specified logging level.

        Args:
            log_level (Level, optional): The initial logging level. Defaults to Level.ERROR.
        """

        self.log_level = log_level

    def log(self, buff, level=Level.ERROR) -> None:
        """
        Logs a message with a given severity level if it meets or exceeds the
        current log level.

        The log message includes a timestamp, the name of the logging level,
        the name of the file from which the log was called,
        and the log message itself.

        Args:
            buff (str): The log message to output.
            level (Level, optional): The severity level of the log message.
            Defaults to Level.ERROR.
        """

        if level.value >= self.log_level.value:
            # Retrieve the file name where the log instance is called
            file_called = inspect.stack()[1].filename.split('/')[-1]
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            print(f"{timestamp}:[{level.name}]:[{file_called}]: {buff}")

    def set_log_level(self, log_level) -> None:
        """
        Sets the logging level of the Log instance.

        Args:
            log_level (Level): The new logging level to be set.
        """

        self.log_level = log_level

    def get_log_level(self) -> Level:
        """
        Retrieves the current logging level of the Log instance.

        Returns:
            Level: The current logging level.
        """

        return self.log_level
