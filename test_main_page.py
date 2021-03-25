from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                    # открываем страницу
    page.should_be_login_link()    # проверяем наличие ссылки на логин-страницу
    page.go_to_login_page()        # переходим на логин-страницу
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()      # проверяем, что перешли на нужную страницу
    login_page.should_be_login_form()     # проверяем наличие формы логина
    login_page.should_be_register_form()  # проверяем наличие формы регистрации

@pytest.mark.basketcheck
def test_guest_should_see_basket_button_on_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_button()

@pytest.mark.basketcheck
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_is_empty()
    basket_page.should_be_message_basket_is_empty()
