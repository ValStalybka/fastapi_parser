import mongomock
import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture()
def client():
    client = TestClient(app)
    return client


@pytest.fixture(autouse=True)
def mongo():
    return mongomock.MongoClient()


@pytest.fixture()
def create_product():
    test_product = {
        "brand": "Nike1",
        "product": "Shoe",
        "price": "1222.00",
        "currency": "p.",
        "gender": "Women",
        "category": "Shoes",
        "url": "/12/",
    }
    return test_product
