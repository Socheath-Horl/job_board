import json
from fastapi.testclient import TestClient

def test_create_user(client: TestClient):
  data = {"username": "testuser", "email": "testuser@example.com", "password": "testing"}
  response = client.post(url="/users/", content=json.dumps(data))
  assert response.status_code == 200
  assert response.json()["email"] == "testuser@example.com"
  assert response.json()["is_active"] == True