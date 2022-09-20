import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


# Тесты main page не сказано маркировать для ревью. Но раз названия совпадают, метку ревью так же оставил
@pytest.mark.login_guest
class TestLoginFromMainPage:
    @staticmethod
    def test_guest_can_go_to_login_page(browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()  # нажатие кнопки, для перехода на LoginPage
        # Инициализация LoginPage в теле теста
        login_page = LoginPage(browser, browser.current_url)
        # после перехода на LoginPage, проверяем, что это действительно LoginPage
        login_page.should_be_login_page()

    @staticmethod
    def test_guest_should_see_login_link(browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_is_empty()  # Проверка, что в корзине нет товара
    basket_page.should_be_message_basket_is_empty()  # Проверка, что есть сообщение о пустой корзине
