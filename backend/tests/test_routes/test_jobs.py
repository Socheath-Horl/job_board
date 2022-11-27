import json

from fastapi.testclient import TestClient


def test_create_job(client: TestClient):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    response = client.post(url="/jobs/", content=json.dumps(data))
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
        "date_posted": "2022-03-20",
    }
    response = client.post(url="/jobs/", content=json.dumps(data))

    response = client.get(url="/jobs/1/")
    assert response.status_code == 200
    assert response.json()["title"] == "SDE super"


def test_read_all_jobs(client: TestClient):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    client.post(url="/jobs/", content=json.dumps(data))
    client.post(url="/jobs/", content=json.dumps(data))

    response = client.get(url="/jobs/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_job(client: TestClient):
    data = {
        "title": "New Job super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "fastapi",
        "date_posted": "2022-03-20",
    }
    client.post(url="/jobs/", content=json.dumps(data))
    data["title"] = "test new title"
    response = client.put(url="/jobs/1", content=json.dumps(data))
    assert response.json()["msg"] == "Successfully updated data."
