from .base_page import BasePage
from final_project.locators import MainPageLocators
from final_project.locators import BasePageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert 'login' in self.url


    def should_be_login_form(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_NAME), 'Field \'Адрес электронной почты \' in login form does not found'


    def should_be_register_form(self):
        assert self.is_element_present(*BasePageLocators.REGISTRATION_NAME), 'Field \'Адрес электронной почты \' in registration form does not found'

    def registr_new_user(self):
        self.click(*BasePageLocators.LOGIN_LINK)
        self.send_keys(*BasePageLocators.REGISTRATION_NAME, words= str(time.time()) + '@fakeemail.org')
        self.click(*BasePageLocators.PASSWORD1)
        self.send_keys(*BasePageLocators.PASSWORD1, words='12587963vL')
        self.click(*BasePageLocators.CONFIRM_PASSWORD)
        self.send_keys(*BasePageLocators.CONFIRM_PASSWORD, words='12587963vL')
        self.click(*BasePageLocators.REG_SUBMIT_BUTTON)

    def check_registr_user(self):
        reg_mes = self.get_text(*BasePageLocators.SUCCESS_MESSAGE_REG)
        self.some_in_something('registering', reg_mes)
        self.should_be_authorized_user()

    def user_can_add_product_to_basket(self):
        self.click(*MainPageLocators.ALL_PRODUCT)
        self.click(*MainPageLocators.BOOK_SHELL_CODERS)
        self.click(*MainPageLocators.BUTTON_ADD_SHOP)
        message_book = 'The shellcoder\'s handbook'
        assert self.some_in_something(message_book, *MainPageLocators.MESSAGE_SHOP)
