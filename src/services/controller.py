from src.services.lamoda import LamodaService


class ServiceController:

    _lamoda = LamodaService

    def __init__(self, db):
        self._db = db

    @property
    def lamoda(self):
        return self._lamoda(self._db.lamoda)
