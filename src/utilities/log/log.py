# -*- coding: utf-8 -*-
# log.py
# Created on: January 22, 2024

import inspect
from datetime import datetime
from ..level import Level


class Log:

    def __init__(self, log_level=Level.ERROR) -> None:
        self.log_level = log_level

    def log(self, buff, level=Level.ERROR) -> None:
        if level.value >= self.log_level.value:
            # Retrieve the file name where the log instance is called
            file_called = inspect.stack()[1].filename.split('/')[-1]
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            print(f"{timestamp}:[{level.name}]:[{file_called}]: {buff}")

    def set_log_level(self, log_level) -> None:
        self.log_level = log_level

    def get_log_level(self) -> Level:
        return self.log_level
