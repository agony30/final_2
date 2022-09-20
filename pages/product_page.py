from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):  # метод для добавления в корзину
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_not_be_success_message(self):  # Проверка, что за отведённое время элемент не появится
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):  # Проверка, что за отведённое время элемент исчезнет
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"

    def should_be_product_add_to_cart_success(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text  # название продукта на странице
        product_name_mess = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text  # продукт в сообщении
        # Проверка на совпадение названия добавленного в корзину продукта
        assert product_name == product_name_mess, 'Название добавленного товара не соответствует товару на странице'
        # Проверка, что сработало специальное предложение со скидкой
        assert self.is_element_present(*ProductPageLocators.OFFER_MESSAGE), 'Специальная скидка не сработала'

    def should_be_basket_price_matches_product_price(self):
        basket_text: str = self.browser.find_element(*ProductPageLocators.BASKET).text  # текст из поля корзины
        basket_total_sum = float(basket_text[basket_text.find('£') + 1:basket_text.find('\n')])  # сумма в корзине
        product_price = float(self.browser.find_element(*ProductPageLocators.PRICE).text[1:])  # цена товара
        assert product_price == basket_total_sum, 'Цена в корзине не равна цене товара'
        print('Сумма корзины:', basket_total_sum)
