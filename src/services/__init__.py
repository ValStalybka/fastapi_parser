from src.dao.mongo import Mongo
from src.services.controller import ServiceController

controller = ServiceController(db=Mongo())
