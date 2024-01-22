# -*- coding: utf-8 -*-
# log.py
# Created on: January 22, 2024
# Last updated on: January 22, 2024# Author(s): remi-boivin

from ..utilities.level import Level


class Log:

    def __init__(self, log_level=Level.Error) -> None:
        self.log_level = log_level
