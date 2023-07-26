from fastapi.testclient import TestClient
from app import app

data_example_1 = {
    "listing_type_id": "free",
    "base_price": 66.0,
    "price": 66.0,
    "initial_quantity": 1,
    "sold_quantity": 0,
    "available_quantity": 1
  }

data_example_2 = {
    "listing_type_id": "freessasd",
    "base_price": 0,
    "price": 0,
    "initial_quantity": 0,
    "sold_quantity": 0,
    "available_quantity": 0
  }

def test_success_prediction():
    endpoint = '/v9/new_or_used/predict'
    body = {"data": data_example_1}
    with TestClient(app) as client:
        response = client.post(endpoint, json=body)
        response_json = response.json()
        assert response.status_code == 200
        assert 'prediction' in response_json

def test_unprocessable_entity():
    endpoint = '/v9/new_or_used/predict'
    body = {"data": data_example_2}
    with TestClient(app) as client:
        response = client.post(endpoint, json=body)
        response_json = response.json()
        assert response.status_code == 422

def test_bad_request():
    endpoint = '/v9/new_or_used/predict'
    body = {"data": [[4.8, 3, 1.4], [2, 1, 3.2, 1.1]]}
    with TestClient(app) as client:
        response = client.post(endpoint, json=body)
        assert response.status_code == 422
