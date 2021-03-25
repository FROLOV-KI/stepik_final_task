from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def add_product_to_basket(self):
         add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
         add_button.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Oops, no such button here!"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12*math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except:
            print("No second alert presented")

    def should_be_added_product_message(self):
        assert self.is_element_present(*ProductPageLocators.INFO_PRODUCT_ADD), "Oops, no added product message here!"
        
    def should_be_basket_total_message(self):
        assert self.is_element_present(*ProductPageLocators.INFO_CURRENT_PRICE), "Oops, no basket total message here!"
    
    def should_be_message_match_added_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        info_product_name = self.browser.find_element(*ProductPageLocators.INFO_PRODUCT_ADD).text
        assert product_name == info_product_name, "Oops, added product message is wrong!"

    def should_be_total_match_added_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        current_price = self.browser.find_element(*ProductPageLocators.INFO_CURRENT_PRICE).text
        assert product_price == current_price, "Oops, basket total message is wrong!"

    def should_not_be_success_message(self):
        assert self.is_not_element_presented(*ProductPageLocators.INFO_PRODUCT_ADD), "Oops, message located, but should not be!"

    def should_be_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.INFO_PRODUCT_ADD), "Oops, message located, but should be disappeared!"
