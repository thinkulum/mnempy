import sys
import os
from configparser import SafeConfigParser
import collections


class Config(collections.UserDict):
    """
    Class for setting settings.
    """

    def __init__(self):
        super(Config, self).__init__()

        # Set default values.
        self.data = {}
