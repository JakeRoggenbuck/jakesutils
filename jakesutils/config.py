import yaml
import json
from enum import Enum
from typeschemalib import typeschemalib
from typing import Union


class ConfigType(Enum):
    JSON = 1
    YAML = 2
    TXT = 3
    STML = 4


class Config:
    def __init__(self, config_path: str, config_type: Union[int, str]):
        """Load file from config_path and get config"""
        self.config_type = ConfigType[config_type.upper()]
        self.config_path = config_path
        config_file = open(self.config_path, 'r')
        self.config = self.get_config(config_file)

    def get_config(self, config):
        """Load config file based on config_type"""
        if self.config_type == ConfigType.JSON:
            return json.load(config)

        elif self.config_type == ConfigType.YAML:
            return yaml.load(config, Loader=yaml.FullLoader)

        elif self.config_type == ConfigType.TXT:
            return config.read()

        elif self.config_type == ConfigType.STML:
            lines = typeschemalib.StmlReader(self.config_path).lines
            return typeschemalib.StmlParser(lines).schema_dict
