from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".register_form .btn-primary")
    

class ProductPageLocators:
    
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    INFO_PRODUCT_ADD = (By.CSS_SELECTOR, "#messages > :nth-child(1) strong")
    
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    INFO_CURRENT_PRICE = (By.CSS_SELECTOR, "#messages > :nth-child(3) strong")


class BasePageLocators:
    
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inv")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a")
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner  h2")
