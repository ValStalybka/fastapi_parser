from pymongo import MongoClient

from src.config import Settings


class Mongo:
    _settings: Settings = Settings()

    def __init__(self):
        self._client = MongoClient(
            host=self._settings.mongo.host, port=self._settings.mongo.port
        )
        self._db = self._settings.mongo.db_name

    @property
    def lamoda(self):
        """returns lamoda collection in the db"""
        return self._client[f"{self._db}"].lamoda

    @property
    def twitch(self):
        """returns twitch collection in the db"""
        return self._client[f"{self._db}"].twitch
