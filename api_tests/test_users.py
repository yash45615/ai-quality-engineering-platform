import pytest

from jsonschema import validate

from api_tests.schemas.user_schema import (
    USER_SCHEMA
)


@pytest.mark.api
@pytest.mark.smoke
def test_get_user(api_client):

    response = api_client.get(
        "/users/1"
    )

    assert response.status_code == 200

    data = response.json()

    validate(
        instance=data,
        schema=USER_SCHEMA
    )

    assert data["id"] == 1


@pytest.mark.api
def test_get_users(api_client):

    response = api_client.get(
        "/users"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(
        data,
        list
    )

    assert len(data) > 0