from typing import Dict
from typing import List
from typing import Union

from bson import ObjectId
from pymongo import ReturnDocument

from src.dao.twitch import TwitchDAO
from src.schemas.twitch import Game
from src.schemas.twitch import Stream
from src.services.redis import cache_result


class TwitchService:
    """class for integrating TwitchAPI calls data to MongoDB"""

    _twitch_access = TwitchDAO()

    def __init__(self, _collection):
        self._collection = _collection

    @property
    def collection(self):
        return self._collection

    def get_object_list(self) -> List:
        obj_list = self.collection.find()
        data = []

        for product in obj_list:
            data.append(product)
        return data

    def get_object(self, obj_id: str) -> Union[Stream, Game]:
        obj = self.collection.find_one({"_id": ObjectId(obj_id)})
        return obj

    def create_object(self, data: Union[Stream, Game]):
        product = self.collection.insert_one(data.model_dump())
        return {"status": 201, "new_object id": str(product.inserted_id)}

    def create_many_objects(self, obj_list: List):
        return self.collection.insert_many(obj_list)

    def update_object(self, obj_id: str, data: Dict) -> Union[Stream, Game]:
        updated_product = self.collection.find_one_and_update(
            {"_id": ObjectId(obj_id)},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )
        return updated_product

    def delete_object(self, obj_id: str) -> Dict:
        result = self.collection.delete_one({"_id": ObjectId(obj_id)})
        if result.deleted_count == 0:
            return {"warning": "nothing deleted, check provided id"}
        return {"objects_deleted": result.deleted_count}


class GameService(TwitchService):
    @cache_result("twitch_games")
    def get_object_list(self):
        return super().get_object_list()


class StreamService(TwitchService):
    @cache_result("twitch_stream")
    def get_object_list(self):
        return super().get_object_list()
