from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time



class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_name = str(time.time()) + "@fakemail.org"
        password = "Az123456789"
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(login_name, password)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.should_not_be_success_message()
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        self.page = ProductPage(browser, link)  
        self.page.open()
        # проверяем, что присутсвует кнопка "Добавить в корзину"
        self.page.should_be_add_to_basket_button()
        # нажимаем на кнопку и добавляем товар в корзину
        self.page.add_product_to_basket()
        # получаем код для решения
        self.page.solve_quiz_and_get_code()
        # проверяем, что появилось сообщение с добавленным товаром
        self.page.should_be_added_product_message()
        # проверяем, что в сообщении о добавленном товаре верное  название товара
        self.page.should_be_message_match_added_product()
        # проверяем, что появилось сообщение с ценой корзины
        self.page.should_be_basket_total_message()
        # проверяем, что в сообщении со стоимостью корзины указана цена товара
        self.page.should_be_total_match_added_product_price()  

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                    marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)  
    page.open()
    # проверяем, что присутсвует кнопка "Добавить в корзину"
    page.should_be_add_to_basket_button()
    # нажимаем на кнопку и добавляем товар в корзину
    page.add_product_to_basket()
    # получаем код для решения
    page.solve_quiz_and_get_code()
    # проверяем, что появилось сообщение с добавленным товаром
    page.should_be_added_product_message()
    # проверяем, что в сообщении о добавленном товаре верное название
    page.should_be_message_match_added_product()
    # проверяем, что появилось сообщение с ценой корзины
    page.should_be_basket_total_message()
    # проверяем, что в сообщении со стоимостью корзины указана цена
    page.should_be_total_match_added_product_price()  



@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.negative
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.negative
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_is_disappeared()


@pytest.mark.logincheck
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
@pytest.mark.logincheck
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.basketcheck
def test_guest_should_see_basket_button_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()

@pytest.mark.need_review
@pytest.mark.basketcheck
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_is_empty()
    basket_page.should_be_message_basket_is_empty()
