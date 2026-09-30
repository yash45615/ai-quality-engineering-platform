import requests


def test_api_health():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert "name" in data
    assert "email" in data