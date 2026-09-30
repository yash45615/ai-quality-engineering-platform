import pytest

from config.settings import settings


@pytest.mark.accessibility
def test_login_page_has_accessible_structure(
    page
):

    page.goto(
        settings.BASE_URL
    )

    snapshot = (
        page.locator("body")
        .aria_snapshot()
    )

    assert snapshot is not None

    assert "Username" in snapshot
    assert "Password" in snapshot