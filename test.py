from jakesutils.config import Config


file = Config("resources/test.yml", "yaml")
print(file.config_type, file.config)
