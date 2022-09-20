from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:first-child strong')
    OFFER_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(2) div strong')
    BASKET = (By.CSS_SELECTOR, '.hidden-xs')
    PRICE = (By.CSS_SELECTOR, 'p.price_color')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")  # invalid selector. For check the tests
    BASKET = (By.CSS_SELECTOR, "span a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "div p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


class RegPageLocators:
    EMAIL_REG = (By.NAME, "registration-email")
    PASSWORD1_REG = (By.NAME, "registration-password1")
    PASSWORD2_REG = (By.NAME, "registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")
