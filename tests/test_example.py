from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_example():
    response = client.get("/example/")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data and "name" in data and "value" in data

def test_create_example():
    payload = {"name": "Test", "value": 123}
    response = client.post("/example/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test"
    assert data["value"] == 123
