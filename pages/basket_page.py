from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)
