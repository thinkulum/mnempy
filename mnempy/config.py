import sys
import os
from configparser import ConfigParser
import collections


class Config(collections.UserDict):
    """
    Class for setting settings.
    """

    def __init__(self, working_dir, config_paths):
        super(Config, self).__init__()

        # Set default values.
        self.data = {}

        config = ConfigParser()
        config.optionxform = lambda option: option

        for config_path in config_paths:
            config.read(config_path)

        for section in config.sections():
            if section not in self.data:
                self.data[section] = {}
            self.data[section].update(config[section])

        self.data['general']['working_dir'] = working_dir
        self.data['general']['build_dir'] = os.path.join(working_dir, 'build')
        self.data['general']['cache_dir'] = os.path.join(working_dir, 'cache')
