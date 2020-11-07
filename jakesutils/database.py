from pymongo import MongoClient
import motor.motor_asyncio as motor


class Database:
    def __init__(
        self,
        host: str = "localhost",
        port: int = 27017,
        is_async: bool = False,
        config: dict = None,
    ):

        self.host = host
        self.port = port
        self.is_async = is_async
        self.config = config

    def connect(self):
        if self.is_async is True:
            self.client = motor.AsyncIOMotorClient(self.host, self.port)
        else:
            self.client = MongoClient(self.host, self.port)

        if self.config is not None:
            self.databases = self.client[self.config["database"]]
            self.collections = [self.client[col] for col in self.config["collections"]]
