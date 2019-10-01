from selenium.common.exceptions import NoSuchElementException
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            x = self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return x

    def click(self, how, what):
        try:
            self.browser.find_element(how, what).click()
        except NoSuchElementException:
            return False
        return True

    def get_text(self, how, what):
        try:
            x = self.browser.find_element(how, what).text
        except NoSuchElementException:
            return 'NoSuchElement'
        return x

    def count_function(self):
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

    def some_in_something(self, what, where):
        try:
            x = str(what) in str(where)
        except NoSuchElementException:
            return False
        return x
