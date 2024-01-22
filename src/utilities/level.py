# -*- coding: utf-8 -*-
# level.py
# Created on: January 22, 2024
# Last updated on: January 22, 2024# Author(s): remi-boivin

from enum import Enum


class Level(Enum):
    """Enum representing log levels."""
    DEBUG = 0
    VERBOSE = 1
    WARNING = 2
    ERROR = 3
