# файл для проверки кусочков кода. Никак не влияет на программу

from .pages import base_page
from selenium.webdriver.common.by import By


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/en-gb/basket/'
    page = base_page.BasePage(browser, link)
    page.open()
    a = page.browser.find_element(By.CSS_SELECTOR, 'div p').text
    print(a)
    if a == 'Your basket is empty. Continue shopping':
        print('!!')
    else:
        print('---')