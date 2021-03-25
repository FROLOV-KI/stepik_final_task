#Базовый класс для сраниц, с которыми будут работать тесты
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators
from .locators import BasketPageLocators

class BasePage():
    def __init__(self, browser, url, timeout=0):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)

    def go_to_basket_page(self):
        button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        button.click()  
    
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        
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

    def is_not_element_presented(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_basket_button(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_BUTTON), "Basket button is not presented"
