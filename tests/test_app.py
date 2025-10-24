import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_index(client):
    resp = client.get("/")
    assert resp.status_code == 200
    json_data = resp.get_json()
    assert json_data["message"] == "Hola, mundo!"

def test_sum_route(client):
    resp = client.get("/sum/4/5")
    assert resp.status_code == 200
    assert resp.get_json()["result"] == 9
