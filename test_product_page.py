from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)                   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.should_be_add_to_basket_button()               # проверяем, что присутсвует кнопка "Добавить в корзину"
    page.add_product_to_basket()                        # нажимаем на кнопку и добавляем товар в корзину
    page.solve_quiz_and_get_code()                      # получаем код для решения
    page.should_be_added_product_message()              # проверяем, что появилось сообщение с добавленным товаром
    page.should_be_message_match_added_product()        # проверяем, что в сообщении о добавленном товаре верное название товара
    page.should_be_basket_total_message()               # проверяем, что появилось сообщение с ценой корзины
    page.should_be_total_match_added_product_price()    # проверяем, что в сообщении со стоимостью корзины указана цена товара

