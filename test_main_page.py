from .pages.main_page import MainPage
from .pages.login_page import LoginPage


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
