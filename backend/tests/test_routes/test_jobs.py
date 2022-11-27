import json
from fastapi.testclient import TestClient


def test_create_job(client: TestClient):
  data = {
    "title": "SDE super",
    "company": "doogle",
    "company_url": "www.doogle.com",
    "location": "USA,NY",
    "description": "python",
    "date_posted": "2022-03-20"
  }
  response = client.post(url="/jobs/create-job/", content=json.dumps(data))
  assert response.status_code == 200
  assert response.json()["company"] == "doogle"
  assert response.json()["description"] == "python"


def test_read_job(client: TestClient):
  data = {
    "title": "SDE super",
    "company": "doogle",
    "company_url": "www.doogle.com",
    "location": "USA,NY",
    "description": "python",
    "date_posted": "2022-03-20"
  }
  response = client.post(url="/jobs/create-job/", content=json.dumps(data))

  response = client.get("/jobs/get/1/")
  assert response.status_code == 200
  assert response.json()['title'] == "SDE super"