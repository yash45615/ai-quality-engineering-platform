import pytest

from appium import webdriver

from appium.options.android import (
    UiAutomator2Options
)

from config.settings import settings


@pytest.fixture
def mobile_driver():

    if not settings.MOBILE_APP:

        pytest.skip(
            "MOBILE_APP is not configured."
        )

    options = UiAutomator2Options()

    options.platform_name = (
        settings.MOBILE_PLATFORM
    )

    options.device_name = (
        settings.MOBILE_DEVICE
    )

    options.app = settings.MOBILE_APP

    driver = webdriver.Remote(
        settings.APPIUM_SERVER,
        options=options
    )

    yield driver

    driver.quit()