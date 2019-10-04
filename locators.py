from selenium.webdriver.common.by import By


class BasePageLocators(object):
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.ID, 'login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, 'login_link_inc')
    LOGIN_NAME = (By.NAME, 'login-username')
    REGISTRATION_NAME = (By.NAME, 'registration-email')
    PASSWORD1 = (By.NAME, 'registration-password1')
    CONFIRM_PASSWORD = (By.NAME, 'registration-password2')
    REG_SUBMIT_BUTTON = (By.NAME, 'registration_submit')
    SUCCESS_MESSAGE_REG = (By.XPATH, '.alert .alertinner.wicon')


class MainPageLocators(object):
    BASKET = (By.XPATH, '/html/body/header/div[1]/div/div[2]/span/a')
    BUTTON_ADD_SHOP = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    MESSAGE_SHOP = (By.XPATH, '//*[@id="messages"]/div[1]/div')
    NAME_OF_PRODUCT = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, '.alert .alertinner p:first-child')
    ALL_PRODUCT = (By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a')
    BOOK_SHELL_CODERS = (By.XPATH, '//*[@id="default"]/div[2]/div/div/div/section/div/ol/li[1]/article/h3/a')


class BasketPageLocators(object):
    BASKET_EMPTY_MESSAGE = (By.ID, 'content_inner')

