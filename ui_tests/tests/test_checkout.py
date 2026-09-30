import pytest

from config.settings import settings

from ui_tests.pages.login_page import (
    LoginPage
)

from ui_tests.pages.inventory_page import (
    InventoryPage
)

from ui_tests.pages.cart_page import (
    CartPage
)

from ui_tests.pages.checkout_page import (
    CheckoutPage
)


@pytest.mark.ui
@pytest.mark.regression
def test_complete_purchase(page):

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

    cart.checkout()

    checkout = CheckoutPage(page)

    checkout.enter_customer_details(
        "Yash",
        "Tester",
        "414001"
    )

    checkout.finish()

    assert (
        checkout.success_message()
        == "Thank you for your order!"
    )