from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        email_field.send_keys(email)
        
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        password_field.send_keys(password)
        
        password_confirm_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM_FIELD)
        password_confirm_field.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверкa на корректный url адрес
        assert "login" in self.browser.current_url, "Wrong page!"

    def should_be_login_form(self):
        # проверкa, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is missing :("

    def should_be_register_form(self):
        # проверкa, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is missing :("
