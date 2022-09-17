import time

import pytest
import faker

from .pages.locators import ProductPageLocators, BasketPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

urls = [f"{product_base_link}/?promo=offer{no}" if no != 7
        else pytest.param(f"{product_base_link}/?promo=offer{no}", marks=pytest.mark.xfail) for no in range(10)]


@pytest.mark.skip
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()  # решение уравнения для вставки ответа
    product_name = page.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text  # название продукта на странице
    product_name_mess = page.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text  # продукт в сообщении
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


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.add_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        'Есть сообщение об успехе после добавления в корзину'


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        'Есть сообщение об успехе после открытия страницы товара'


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.add_to_basket()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        'Тестовое сообщение не исчезло после добавления товара в корзину'


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    assert page.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "В корзине есть товар"
    assert page.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Нет сообщения, что корзина пуста"


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        f = faker.Faker()
        email = f.email()
        p = faker.Faker()
        password = p.password()
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = product_base_link
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        # page.solve_quiz_and_get_code()  # решение уравнения для вставки ответа. Расскоментировать, если нужно
        product_name = page.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # название продукта на странице
        product_name_mess = page.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text  # продукт в сообщении
        # Проверка на совпадение названия добавленного в корзину продукта
        assert product_name == product_name_mess, 'Название добавленного товара не соответствует товару на странице'
        # Проверка, что сработало специальное предложение со скидкой
        assert page.is_element_present(*ProductPageLocators.OFFER_MESSAGE), 'Специальная скидка не сработала'
        print('Товар успешно добавлен в корзину')

        # проверка на равенство цены в корзине после добавления товара, и цены самого товара
        basket_text: str = page.browser.find_element(*ProductPageLocators.BASKET).text  # текст из поля корзины
        basket_total_sum = float(basket_text[basket_text.find('£') + 1:basket_text.find('\n')])  # сумма в корзине
        assert float(
            page.browser.find_element(*ProductPageLocators.PRICE).text[1:]) == basket_total_sum, 'Цена не равна'
        print('Сумма корзины:', basket_total_sum)

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_base_link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Есть сообщение об успехе после открытия страницы товара'
