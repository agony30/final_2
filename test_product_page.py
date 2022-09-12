from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()  # решение уравнения для вставки ответа
    product_name = page.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text  # название продукта на странице
    product_name_mess = page.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text  # продукт в сообщении
    # Проверка на совпадение названия добавленного в корзину продукта
    assert product_name == product_name_mess, 'Название добавленного товара не соответствует товару на странице'
    # Проверка, что сработало специальное предложение со скидкой
    assert page.is_element_present(*ProductPageLocators.OFFER_MESSAGE), 'Специальная скидка не сработала'
    print('Товар успешно добавлен в корзину')

    # проверка на равенство цены в корзине после добавления товара, и цены самого товара
    basket_text: str = page.browser.find_element(*ProductPageLocators.BASKET).text  # текст из поля корзины
    basket_total_sum = float(basket_text[basket_text.find('£') + 1:basket_text.find('\n')])  # сумма в корзине
    assert float(page.browser.find_element(*ProductPageLocators.PRICE).text[1:]) == basket_total_sum, 'Цена не равна'
    print('Сумма корзины:', basket_total_sum)

