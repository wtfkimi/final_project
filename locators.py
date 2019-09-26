from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_lINK = (By.ID, 'login_link')
    LOGIN_NAME = (By.NAME, 'login-username')
    REGISTRATION_NAME = (By.NAME, 'registration-email')