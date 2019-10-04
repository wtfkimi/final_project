from selenium.common.exceptions import NoSuchElementException
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from final_project.locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10): # Конструктор
        self.browser = browser
        self.url = url


    def count_function(self): # Функция подсчета
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print("Your code: {}".format(alert_text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def click(self, how, what): # Клик
        try:
            self.browser.find_element(how, what).click()
        except NoSuchElementException:
            return False
        return True


    def get_text(self, how, what): #Получить текст
        try:
            x = self.browser.find_element(how, what).text
        except NoSuchElementException:
            return 'NoSuchElement'
        return x


    def go_to_login_page(self): #Перейти на логин стр
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()


    def is_element_present(self, how, what): #Найти элемент
        try:
            x = self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return x


    def is_disappeared(self, how, what, timeout=4): #Будет ждать пока элемент не исчезнет
        try:
            WebDriverWait(self.browser, timeout, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    def is_not_element_present(self, how, what, timeout=4): #Упадет как только увидит искомый элемент
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False


    def open(self): #Открыть юрл
        self.browser.get(self.url)


    def send_keys(self, how, what, words): #Передать текст
        try:
            x = self.browser.find_element(how, what).send_keys('{}'.format(words))
        except NoSuchElementException:
            return False
        return x


    def should_be_authorized_user(self): #Проверить авторизацию
        assert self.is_element_present(*BasePageLocators.USER_ICON)


    def should_be_login_link(self): #Проверить что линк логин присутствует
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    def some_in_something(self, what, where): # Проверка элемента в строке
        try:
            x = str(what) in str(where)
        except NoSuchElementException:
            return 'Элемент нет в строке или в чем-то другом'
        return x








