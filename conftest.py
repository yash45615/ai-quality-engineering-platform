import pytest
from playwright.sync_api import sync_playwright

from config.settings import settings
from utils.screenshots import take_screenshot


# Load custom fixtures
pytest_plugins = [
    "fixtures.api_fixtures",
    "fixtures.mobile_fixtures",
]


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, settings.BROWSER)

        browser = browser_type.launch(
            headless=settings.HEADLESS
        )

        yield browser

        browser.close()


@pytest.fixture
def page(browser, request):
    context = browser.new_context(
        viewport={
            "width": 1440,
            "height": 900
        },
        record_video_dir="reports/videos"
    )

    page = context.new_page()

    yield page

    test_failed = (
        hasattr(request.node, "rep_call")
        and request.node.rep_call.failed
    )

    if test_failed:
        try:
            take_screenshot(
                page,
                request.node.nodeid
            )
        except Exception:
            pass

    context.close()


@pytest.hookimpl(
    hookwrapper=True,
    tryfirst=True
)
def pytest_runtest_makereport(item, call):
    outcome = yield

    rep = outcome.get_result()

    setattr(
        item,
        f"rep_{rep.when}",
        rep
    )