import pytest

from config.settings import settings
from ui_tests.pages.login_page import LoginPage
from ui_tests.pages.inventory_page import InventoryPage
from ui_tests.pages.cart_page import CartPage


@pytest.mark.ui
@pytest.mark.regression
def test_open_cart(page):

    login = LoginPage(page)

    login.open(
        settings.BASE_URL
    )

    login.login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(page)

    inventory.add_backpack()

    inventory.open_cart()

    cart = CartPage(page)

    assert page.url.endswith(
        "/cart.html"
    )

    assert cart.get_item_name() == (
        "Sauce Labs Backpack"
    )