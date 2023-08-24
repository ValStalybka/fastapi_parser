from bson import ObjectId
from pymongo import ReturnDocument


class LamodaService:
    def __init__(self, _collection):
        self._collection = _collection

    @property
    def collection(self):
        return self._collection

    def list_products(self):
        product_list = self.collection.find({})
        data = []

        for product in product_list:
            data.append(product)
        return data

    def get_product(self, product_id: str):
        product = self.collection.find_one({"_id": ObjectId(product_id)})
        return product

    def create_product(self, data):
        product = self.collection.insert_one(data.model_dump())
        return {"status": 201, "new_object id": str(product.inserted_id)}

    def update_product(self, product_id, data):
        updated_product = self.collection.find_one_and_update(
            {"_id": ObjectId(product_id)},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )
        return updated_product

    def delete_object(self, product_id):
        result = self.collection.delete_one({"_id": ObjectId(product_id)})
        if result.deleted_count == 0:
            return {"warning": "nothing deleted, check provided id"}
        return {"objects_deleted": result.deleted_count}
