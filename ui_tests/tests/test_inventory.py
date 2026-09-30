import pytest

from config.settings import settings

from ui_tests.pages.login_page import (
    LoginPage
)

from ui_tests.pages.inventory_page import (
    InventoryPage
)


@pytest.mark.ui
@pytest.mark.smoke
def test_add_product_to_cart(page):

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

    assert (
        inventory.cart_count()
        == "1"
    )