from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = 'http://selenium1py.pythonanywhere.com'

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)# инициалиазация MainPage
    page.open() #Вызвать метод 'открыть' сайт
    page.go_to_login_page() # Найти селектор логин стр, кликнуть
    login_page = LoginPage(browser, browser.current_url) #Инициализировать класс LoginPage
    login_page.should_be_login_page()# Выполнить проверки

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()



