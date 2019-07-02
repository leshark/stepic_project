from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    WATCH_CART_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONF_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT = (By.NAME, "registration_submit")


class ProductPageLocators:
    CART_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    MESSAGE_NAME = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) .alertinner strong")
    MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) .alertinner strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) .alertinner")


class CartPageLocators:
    IS_CART_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    CART_ITEMS = (By.CSS_SELECTOR, "#content_inner .basket-items")
