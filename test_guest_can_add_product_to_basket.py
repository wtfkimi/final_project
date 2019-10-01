import self as self

from .pages.product_page import ProductPage
import pytest
bugged_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7' # BUGGED Link


one_more_product_page = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{x}" for x in range(10)]

@pytest.mark.skip
@pytest.mark.skip('bugged_link', bugged_link)
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_add_product_to_basket()


@pytest.mark.negative
@pytest.mark.xfail(reason='negative_test')
def test_test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = product_base_link
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_see_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    link = product_base_link
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_cant_see_success_message()


@pytest.mark.negative
@pytest.mark.xfail(reason='negative_test')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = product_base_link
    page = ProductPage(browser, link)
    page.open()
    page.test_message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = one_more_product_page
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = one_more_product_page
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


