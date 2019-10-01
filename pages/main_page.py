from .base_page import BasePage
from selenium.webdriver.common.by import By
from final_project.locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_lINK)
        login_link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_lINK), 'Login link doesn\'t presented'