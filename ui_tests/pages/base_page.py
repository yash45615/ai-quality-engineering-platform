from playwright.sync_api import (
    Page,
    expect
)


class BasePage:

    def __init__(
        self,
        page: Page
    ):

        self.page = page

    def goto(
        self,
        url: str
    ):

        self.page.goto(
            url,
            wait_until="domcontentloaded"
        )

    def click(
        self,
        selector: str
    ):

        self.page.locator(
            selector
        ).click()

    def fill(
        self,
        selector: str,
        value: str
    ):

        self.page.locator(
            selector
        ).fill(value)

    def expect_visible(
        self,
        selector: str
    ):

        expect(
            self.page.locator(selector)
        ).to_be_visible()

    def get_title(self):

        return self.page.title()