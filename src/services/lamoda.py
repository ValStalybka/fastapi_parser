from typing import Dict
from typing import List

from bson import ObjectId
from pymongo import ReturnDocument

from src.schemas.lamoda import Product


class LamodaService:
    def __init__(self, _collection):
        self._collection = _collection

    @property
    def collection(self):
        return self._collection

    def list_products(self) -> List:
        product_list = self.collection.find({})
        data = []

        for product in product_list:
            data.append(product)
        return data

    def get_product(self, product_id: str) -> Product:
        product = self.collection.find_one({"_id": ObjectId(product_id)})
        return product

    def create_product(self, data: Product) -> Dict:
        product = self.collection.insert_one(data.model_dump())
        return {"status": 201, "new_object id": str(product.inserted_id)}

    def create_many_products(self, data: List) -> Dict:
        result = self._collection.insert_many(data)
        return {"status": 201, "created objects count": len(result.inserted_ids)}

    def update_product(self, product_id: str, data: Dict) -> Product:
        updated_product = self.collection.find_one_and_update(
            {"_id": ObjectId(product_id)},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )
        return updated_product

    def delete_object(self, product_id: str) -> Dict:
        result = self.collection.delete_one({"_id": ObjectId(product_id)})
        if result.deleted_count == 0:
            return {"warning": "nothing deleted, check provided id"}
        return {"objects_deleted": result.deleted_count}
