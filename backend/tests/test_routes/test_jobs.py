import json

from fastapi import status
from fastapi.testclient import TestClient


def test_create_job(client: TestClient, normal_user_token_headers):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    response = client.post(
        url="/jobs/", content=json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 200
    assert response.json()["company"] == "doogle"
    assert response.json()["description"] == "python"


def test_read_job(client: TestClient, normal_user_token_headers):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    response = client.post(
        url="/jobs/", content=json.dumps(data), headers=normal_user_token_headers
    )

    response = client.get(url="/jobs/1/")
    assert response.status_code == 200
    assert response.json()["title"] == "SDE super"


def test_read_all_jobs(client: TestClient, normal_user_token_headers):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    client.post(
        url="/jobs/", content=json.dumps(data), headers=normal_user_token_headers
    )
    client.post(
        url="/jobs/", content=json.dumps(data), headers=normal_user_token_headers
    )

    response = client.get(url="/jobs/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_job(client: TestClient, normal_user_token_headers):
    data = {
        "title": "New Job super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "fastapi",
        "date_posted": "2022-03-20",
    }
    client.post(
        url="/jobs/", content=json.dumps(data), headers=normal_user_token_headers
    )
    data["title"] = "test new title"
    response = client.put(
        url="/jobs/1", content=json.dumps(data), headers=normal_user_token_headers
    )
    assert response.json()["msg"] == "Successfully updated data."


def test_delete_a_job(client: TestClient, normal_user_token_headers):
    data = {
        "title": "New Job super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "fastapi",
        "date_posted": "2022-03-20",
    }
    client.post(
        url="/jobs/", content=json.dumps(data), headers=normal_user_token_headers
    )
    client.delete(url="/jobs/1", headers=normal_user_token_headers)
    response = client.get(url="/jobs/1")
    assert response.status_code == status.HTTP_404_NOT_FOUND
