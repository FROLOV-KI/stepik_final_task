#Базовый класс для сраниц, с которыми будут работать тесты
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            alert = self.browser.switch_to.alert
        except NoAlertPresentException:
            return False
        return True
