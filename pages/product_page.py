from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):  # метод для добавления в корзину
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

