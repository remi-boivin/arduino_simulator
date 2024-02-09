# -*- coding: utf-8 -*-
# log.py
# Created on: January 22, 2024
# Last updated on: January 22, 2024# Author(s): remi-boivin

from ..level import Level
import inspect


class Log:

    def __init__(self, log_level=Level.ERROR) -> None:
        self.log_level = log_level

    def log(self, buff, level=Level.ERROR) -> None:
        if level.value >= self.log_level.value:
            file_called = inspect.stack()[1][1].split('/')[9]
            print(f"[{level.name}]:[{file_called}.py]: {buff}")

    def set_log(self, log_level) -> None:
        self.log_level = log_level

    def get_log_level(self) -> Level:
        return self.log_level
