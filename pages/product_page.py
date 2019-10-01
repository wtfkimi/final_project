from .base_page import BasePage
from final_project.locators import MainPageLocators
import time
class ProductPage(BasePage):
    def test_guest_can_add_product_to_basket(self):
        self.names_of_product()
        self.check_and_click_on_button_add()
        self.guest_can_count_function_get_code()
        self.check_message()
        self.check_product_price()
        self.check_all_mesage()

    def test_guest_can_see_success_message_after_adding_product_to_basket(self):
        self.check_and_click_on_button_add()
        assert self.is_not_element_present(*MainPageLocators.MESSAGE_SHOP)

    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*MainPageLocators.MESSAGE_SHOP)

    def test_message_disappeared_after_adding_product_to_basket(self):
        self.check_and_click_on_button_add()
        time.sleep(2)
        assert  self.is_disappeared(*MainPageLocators.MESSAGE_SHOP)


    def check_and_click_on_button_add(self):
        #assert self.is_element_present(*MainPageLocators.BUTTON_ADD_SHOP), 'Element does\'t present'
        self.click(*MainPageLocators.BUTTON_ADD_SHOP)

    def names_of_product(self):
        self.name_product = self.get_text(*MainPageLocators.NAME_OF_PRODUCT)

    def guest_can_count_function_get_code(self):
        self.count_function()

    def check_message(self):
        message_shop = self.get_text(*MainPageLocators.MESSAGE_SHOP)
        self.some_in_something(self.name_product, message_shop)


    def check_product_price(self):
        product_text_price = self.get_text(*MainPageLocators.PRODUCT_PRICE)
        product_price_message = self.get_text(*MainPageLocators.PRODUCT_PRICE_MESSAGE)
        self.some_in_something(product_text_price, product_price_message)

    def check_all_mesage(self):
       x = self.get_text(*MainPageLocators.MESSAGE_SHOP)
       assert x == 'Coders at Work был добавлен в вашу корзину.', 'Элемента нет в корзине'




