import time
import pytest

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
promo_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"  # email generate
        password = str(time.time()) + "fakepass"  # password generate
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)  # регистрация пользователя
        page.should_be_authorized_user()  # проверка, что пользователь выполнил вход

    def test_user_can_add_product_to_basket(self, browser):
        link = promo_link
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()  # решение уравнения для вставки ответа
        page.should_be_product_add_to_cart_success()  # проверка, что товар успешно добавлен
        page.should_be_basket_price_matches_product_price()  # проверка, что цена в корзине совпадает с ценой товара

    @pytest.mark.skip  # тест не требуется для ревью
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_base_link)
        page.open()
        page.should_not_be_success_message()


urls = [f"{product_base_link}/?promo=offer{no}" if no != 7
        else pytest.param(f"{product_base_link}/?promo=offer{no}", marks=pytest.mark.xfail) for no in range(6, 10)]


# 1 тест помечен как xfail. Тест специально оставил с "параметризацией", как пример для обучения.
# Промо-страницы взял не все, а только с 6 по 9 (для ускорения проверок)
@pytest.mark.need_review
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()  # решение уравнения для вставки ответа
    page.should_be_product_add_to_cart_success()  # проверка, что товар успешно добавлен
    page.should_be_basket_price_matches_product_price()  # проверка, что цена в корзине совпадает с ценой товара


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_is_empty()  # Проверка, что в корзине нет товара
    basket_page.should_be_message_basket_is_empty()  # Проверка, что есть сообщение о пустой корзине


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


#  Тесты ниже не входят в ревью. Все помечены меткой "skip"


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.add_to_basket()
    page.should_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
