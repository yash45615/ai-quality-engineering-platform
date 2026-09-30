from playwright.sync_api import Page, expect

from ui_tests.pages.base_page import BasePage


class CartPage(BasePage):

    CHECKOUT = "#checkout"
    CART_ITEM_NAME = ".cart_item .inventory_item_name"

    def __init__(self, page: Page):
        super().__init__(page)

    def checkout(self):
        self.click(self.CHECKOUT)

    def get_item_name(self):
        return self.page.locator(
            self.CART_ITEM_NAME
        ).first.inner_text()