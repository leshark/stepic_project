import time

import pytest

from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
offer_urls = [product_base_link + "/?promo=offer" + str(num) for num in range(9)]


class TestUserAddToCartFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, product_base_link)
        page.open()
        page.go_to_login_page()
        mail = str(time.time()) + "@fakemail666.org"
        pasw = str(time.time()) + "_some_salt_lol"  # nice cryptography
        page.register_new_user(mail, pasw)
        page.should_be_authorized_user()

        self.browser = page.browser

    def test_user_cant_see_success_message(self):
        page = ProductPage(self.browser, product_base_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self):
        page = ProductPage(self.browser, product_base_link)
        page.open()
        page.add_to_cart()
        page.check_add_to_cart_message()


@pytest.mark.skip(reason="Takes too much time :)")
@pytest.mark.parametrize('link', offer_urls)
def test_guest_can_add_promo_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_add_to_cart_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.add_to_cart()
    page.check_add_to_cart_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.go_to_cart_page()
    page = CartPage(page.browser, browser.current_url)
    page.open()
    page.are_items_in_cart()
    page.is_cart_empty()
