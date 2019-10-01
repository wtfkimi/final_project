from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

link = 'http://selenium1py.pythonanywhere.com/en-gb'
link_product_page = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/'

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)# инициалиазация MainPage
    page.open() #Вызвать метод 'открыть' сайт
    page.go_to_login_page() # Найти селектор логин стр, кликнуть
    login_page = LoginPage(browser, browser.current_url) #Инициализировать класс LoginPage
    login_page.should_be_login_page()# Выполнить проверки

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.test_guest_cant_see_product_in_basket_opened_from_main_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link_product_page)
    page.open()
    page.test_guest_cant_see_product_in_basket_opened_from_product_page()

