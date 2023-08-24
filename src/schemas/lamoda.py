from datetime import datetime

from pydantic import BaseModel


class Product(BaseModel):
    brand: str
    product: str
    price: str
    currency: str
    gender: str
    category: str
    url: str
    created_at: datetime = datetime.now()
