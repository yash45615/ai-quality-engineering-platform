from playwright.sync_api import Page

from ui_tests.pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(
        self,
        page: Page
    ):

        super().__init__(page)

    def open(
        self,
        base_url: str
    ):

        self.goto(base_url)

    def login(
        self,
        username: str,
        password: str
    ):

        self.fill(
            self.USERNAME,
            username
        )

        self.fill(
            self.PASSWORD,
            password
        )

        self.click(
            self.LOGIN_BUTTON
        )

    def error_visible(self):

        return self.page.locator(
            self.ERROR_MESSAGE
        ).is_visible()