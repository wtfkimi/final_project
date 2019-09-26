from .base_page import BasePage
from final_project.locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.url


    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_NAME), 'Field \'Адрес электронной почты \' in login form does not found'


    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REGISTRATION_NAME), 'Field \'Адрес электронной почты \' in registration form does not found'

