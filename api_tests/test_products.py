import pytest


@pytest.mark.api
def test_get_products(api_client):

    response = api_client.get(
        "/posts"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(
        data,
        list
    )

    assert len(data) > 0


@pytest.mark.api
def test_create_product(api_client):

    payload = {
        "title": "Automation Test Product",
        "body": "Created by API automation",
        "userId": 1
    }

    response = api_client.post(
        "/posts",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["userId"] == 1