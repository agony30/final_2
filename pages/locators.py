from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div h1')
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, '#messages div:first-child strong')
    OFFER_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(2) div strong')
    BASKET = (By.CSS_SELECTOR, '.hidden-xs')
    PRICE = (By.CSS_SELECTOR, 'p.price_color')

