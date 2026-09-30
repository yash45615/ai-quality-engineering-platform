import pytest

from api_tests.clients.api_client import APIClient
from config.settings import settings


@pytest.fixture
def api_client():
    client = APIClient(
        settings.API_BASE_URL
    )

    yield client

    client.close()