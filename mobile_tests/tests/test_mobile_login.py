import pytest

from mobile_tests.pages.login_page import (
    MobileLoginPage
)


@pytest.mark.mobile
def test_mobile_login(
    mobile_driver
):

    page = MobileLoginPage(
        mobile_driver
    )

    page.enter_username(
        "testuser"
    )

    page.enter_password(
        "password"
    )

    page.login()