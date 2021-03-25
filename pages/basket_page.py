from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_be_basket_is_empty(self):
        assert self.is_not_element_presented(*BasketPageLocators.BASKET_CONTENT), "Oops, something in the basket, but should not be!"

    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Oops, message is missing!"  
