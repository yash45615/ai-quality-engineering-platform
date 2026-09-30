import pytest


@pytest.mark.api
def test_authorization_header_is_sent(
    api_client
):

    token = "test-token"

    response = api_client.get(
        "/users/1",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200