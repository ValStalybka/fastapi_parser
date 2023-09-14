from src.dao.twitch import TwitchDAO
from src.services.lamoda import LamodaService
from src.services.twitch import TwitchService


class ServiceController:
    _lamoda = LamodaService
    _twitch = TwitchService
    _twitch_dao = TwitchDAO()

    def __init__(self, db):
        self._db = db

    @property
    def lamoda(self):
        return self._lamoda(self._db.lamoda)

    @property
    def games(self):
        return self._twitch(self._db.twitch_games)

    @property
    def streams(self):
        return self._twitch(self._db.twitch_streams)

    @property
    def twitch_dao(self):
        return self._twitch_dao
