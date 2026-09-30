from playwright.sync_api import Page

from ui_tests.pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE = "#continue"
    FINISH = "#finish"

    SUCCESS_MESSAGE = ".complete-header"

    def __init__(
        self,
        page: Page
    ):

        super().__init__(page)

    def enter_customer_details(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ):

        self.fill(
            self.FIRST_NAME,
            first_name
        )

        self.fill(
            self.LAST_NAME,
            last_name
        )

        self.fill(
            self.POSTAL_CODE,
            postal_code
        )

        self.click(
            self.CONTINUE
        )

    def finish(self):

        self.click(
            self.FINISH
        )

    def success_message(self):

        return self.page.locator(
            self.SUCCESS_MESSAGE
        ).inner_text()