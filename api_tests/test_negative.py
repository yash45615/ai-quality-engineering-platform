import pytest


@pytest.mark.api
@pytest.mark.regression
def test_user_not_found(api_client):

    response = api_client.get(
        "/users/999999"
    )

    assert response.status_code == 404