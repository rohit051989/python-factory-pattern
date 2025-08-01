from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_example():
    response = client.get("/example/")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data and "name" in data and "value" in data

    payload = {"name": "Test", "value": 123}
    response = client.post("/example/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test"
    assert data["value"] == 123

def test_create_example():
    payload = {"name": "Test", "value": 123}
    response = client.post("/example/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test"
    assert data["value"] == 123

def test_get_customers():
    response = client.get("/example/customers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_customer_by_email():
    # This test assumes a customer with email 'test@example.com' exists in the DB
    response = client.get("/example/customers/by-email/test@example.com")
    if response.status_code == 200:
        data = response.json()
        assert data["email"] == "test@example.com"
    else:
        assert response.status_code == 404
