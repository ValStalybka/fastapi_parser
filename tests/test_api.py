import json


def test_backend_connection(client):
    response = client.get("/lamoda/products")
    assert response.status_code == 200


def test_db_connection(mongo):
    server_status = mongo.server_info()
    assert server_status["ok"] == 1.0


def test_create_product(client, create_product):
    response = client.post("/lamoda/products", content=json.dumps(create_product))
    assert response.status_code == 201
