from src.dao.mongo import Mongo
from src.dao.twitch import TwitchDAO
from src.services.lamoda import LamodaService
from src.services.twitch import GameService
from src.services.twitch import StreamService


class ServiceController:
    _lamoda = LamodaService
    _games = GameService
    _streams = StreamService
    _twitch_dao = TwitchDAO()

    def __init__(self, db: Mongo):
        self._db = db

    @property
    def lamoda(self):
        return self._lamoda(self._db.lamoda)

    @property
    def games(self):
        return self._games(self._db.twitch_games)

    @property
    def streams(self):
        return self._streams(self._db.twitch_streams)

    @property
    def twitch_dao(self):
        return self._twitch_dao
