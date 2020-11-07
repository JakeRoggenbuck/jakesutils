from jakesutils.config import Config

file = Config("resources/test.yml", "yaml")
print(file.config_type, file.config)


from jakesutils.download import download_file

download_file("https://jr0.org/impulse/list.json", "list.json")


from jakesutils.database import Database

db_config = {"database": "my_database", "collections": ["my_col_1", "my_col_2"]}

db_1 = Database()
db_1.connect()
print(db_1.client)

db_3 = Database(config=db_config)
db_3.connect()
print(db_3.collections)
