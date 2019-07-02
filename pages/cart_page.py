from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def is_cart_empty(self):
        assert self.browser.find_element(
            *CartPageLocators.IS_CART_EMPTY).text == "Your basket is empty. Continue shopping", "Cart seems not being empty"

    def are_items_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEMS), "There are products in the cart"
