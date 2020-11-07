from jakesutils.config import Config
from jakesutils.download import download_file


file = Config("resources/test.yml", "yaml")
print(file.config_type, file.config)

download_file("https://jr0.org/impulse/list.json", "list.json")
