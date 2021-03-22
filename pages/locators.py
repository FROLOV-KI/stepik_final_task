from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    INFO_PRODUCT_ADD = (By.CSS_SELECTOR, "#messages > :nth-child(1) strong")
    
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    INFO_CURRENT_PRICE = (By.CSS_SELECTOR, "#messages > :nth-child(3) strong") 

