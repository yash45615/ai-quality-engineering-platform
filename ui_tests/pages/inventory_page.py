from playwright.sync_api import Page

from ui_tests.pages.base_page import BasePage


class InventoryPage(BasePage):

    ADD_BACKPACK = (
        "#add-to-cart-sauce-labs-backpack"
    )

    CART = ".shopping_cart_link"

    TITLE = ".title"

    def __init__(
        self,
        page: Page
    ):

        super().__init__(page)

    def add_backpack(self):

        self.click(
            self.ADD_BACKPACK
        )

    def open_cart(self):

        self.click(
            self.CART
        )

    def cart_count(self):

        return self.page.locator(
            self.CART
        ).inner_text()