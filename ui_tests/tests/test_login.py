import pytest

from config.settings import settings

from ui_tests.pages.login_page import (
    LoginPage
)


@pytest.mark.ui
@pytest.mark.smoke
def test_valid_login(page):

    login_page = LoginPage(page)

    login_page.open(
        settings.BASE_URL
    )

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert page.url.endswith(
        "/inventory.html"
    )


@pytest.mark.ui
@pytest.mark.regression
def test_invalid_login(page):

    login_page = LoginPage(page)

    login_page.open(
        settings.BASE_URL
    )

    login_page.login(
        "invalid_user",
        "wrong_password"
    )

    assert (
        login_page.error_visible()
        is True
    )