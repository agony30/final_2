from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):  # метод для добавления в корзину
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

