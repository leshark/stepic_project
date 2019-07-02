from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.CART_LINK)
        add_button.click()

    def check_add_to_cart_message(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME)
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE)

        assert price and name and message_name and message_price, "Not all elements are presented"

        print(name.text, message_name.text)
        assert name.text == message_name.text, "Product names do not match"
        assert price.text == message_price.text, "Product prices do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but remains on page"
