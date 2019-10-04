from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest
from .pages.basket_page import BasketPage

bugged_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7' # BUGGED Link


link_product_page = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/'
link_for_registr = 'http://selenium1py.pythonanywhere.com/en-gb'


urls = [f"{link_product_page}/?promo=offer{x}" for x in range(10)]
@pytest.mark.need_review
@pytest.mark.skip('bugged_link', bugged_link)
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_add_product_to_basket()


@pytest.mark.negative
@pytest.mark.xfail(reason='negative_test')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = link_product_page
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_see_success_message_after_adding_product_to_basket()


def test_user_cant_see_success_message(browser):
    link = link_product_page
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_cant_see_success_message()


@pytest.mark.negative
@pytest.mark.xfail(reason='negative_test')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = link_product_page
    page = ProductPage(browser, link)
    page.open()
    page.test_message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = link_product_page
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = link_product_page
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    page = LoginPage(browser, link_for_registr)
    page.open()
    page.registr_new_user()
    page.user_can_add_product_to_basket()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link_product_page)
    page.open()
    page.test_guest_cant_see_product_in_basket_opened_from_product_page()


@pytest.mark.check_registration
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link_for_registr)
        page.open()
        page.registr_new_user()


    def test_regist_user(self,browser):
        page = LoginPage(browser, link_for_registr)
        page.check_registr_user()


