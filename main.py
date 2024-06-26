import time
from credentials import *
from Steps.Cart_steps import *
from Steps.Login_page import *
from Steps.Shop_steps import *


def test_correct_login(driver):
    wait_page_open(driver)  # ждем открытия страницы
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    logo_text = driver.find_element(*PageObject.SauceDemo.LoginPage.logo_text)  # находим лого страницы
    assert logo_text.text == "Swag Labs"  # проверяем что он есть


def test_incorrect_login(driver):
    wait_page_open(driver)  # ждем открытия страницы
    login_method(driver, incorrect_login, incorrect_password)  # вводим логин, пароль, логинимся
    err_msg = driver.find_element(*PageObject.SauceDemo.LoginPage.error_msg)  # находим ошибку
    assert err_msg.text == PageObject.SauceDemo.LoginPage.err_msg_text  # сверяем текст ошибки


def test_add_item_in_cart_from_shop(driver):
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    add_to_cart(driver, PageObject.SauceDemo.ShopPage.backpack_add_to_cart_btn)  # добавляем в корзину
    go_to_cart(driver)  # переходим в корзину
    # сверяем, что товар в корзине
    assert get_text(driver, PageObject.SauceDemo.ShopPage.item_in_cart) == "Sauce Labs Backpack"


def test_delete_item_from_cart(driver):
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    add_to_cart(driver, PageObject.SauceDemo.ShopPage.backpack_add_to_cart_btn)  # добавляем в корзину
    go_to_cart(driver)  # переходим в корзину
    name = find_item_by_name(driver, "Sauce Labs Backpack")
    assert name.text == "Sauce Labs Backpack"  # сверяем, что товар в корзине
    cart_loc = driver.find_element(By.CLASS_NAME, "cart_list")  # находим элемент товаров в корзине
    cart_len_before = cart_loc.find_elements(By.CSS_SELECTOR, "*")  # находим их длинну
    delete_item(driver)  # очищаем корзину
    cart_loc = driver.find_element(By.CLASS_NAME, "cart_list")  # повторяем поиск элементов корзины
    cart_len_after = cart_loc.find_elements(By.CSS_SELECTOR, "*")  # находим их длинну
    assert len(cart_len_before) > len(cart_len_after)  # сверяем, что после удаления элементов меньше


def test_add_item_from_description(driver):
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    item = find_item_by_name(driver, "Sauce Labs Backpack")  # находим товар
    item.click()  # открываем его
    add_to_cart(driver, PageObject.SauceDemo.ItemDescription.add_btn)  # добавляем в корзину
    name = find_item_by_name(driver, "Sauce Labs Backpack")  # находим имя
    assert name.text == "Sauce Labs Backpack"  # сверяем, что оно верное


def test_delete_item_from_description(driver):
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    item = find_item_by_name(driver, "Sauce Labs Backpack")  # находим товар по имени
    item.click()  # открываем его
    add_to_cart(driver, PageObject.SauceDemo.ItemDescription.add_btn)  # добавляем в корзину
    delete_item(driver)  # удаляем его


def test_item_description_by_name(driver):
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    item = find_item_by_name(driver, "Sauce Labs Backpack")  # находим товар по имени
    item.click()  # открываем его
    description = driver.find_element(*PageObject.SauceDemo.ItemDescription.description)
    assert description  # сверяем, что элемент описания товара есть на странице


def test_item_description_by_image(driver):
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    item = find_item_by_img_name(driver, "Sauce Labs Backpack")  # находим товар по имени картинки
    item.click()  # открываем его
    description = driver.find_element(*PageObject.SauceDemo.ItemDescription.description)
    assert description  # сверяем, что элемент описания товара есть на странице


def test_purchase_complete(driver):
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    add_to_cart(driver, PageObject.SauceDemo.ShopPage.backpack_add_to_cart_btn)  # добавляем в корзину
    go_to_cart(driver)  # переходим в корзину
    click_element(driver, PageObject.SauceDemo.CartCheckout.checkout_btn)  # жмем кнопку в чекаут
    enter_text(driver, PageObject.SauceDemo.CartCheckout.first_n, first_name)  # вводим имя
    enter_text(driver, PageObject.SauceDemo.CartCheckout.last_n, last_name)  # вводим фамилию
    enter_text(driver, PageObject.SauceDemo.CartCheckout.postal_code, zip_code)  # вводим индекс
    click_element(driver, PageObject.SauceDemo.CartCheckout.continue_btn)  # жмем далее
    click_element(driver, PageObject.SauceDemo.CartCheckout.finish_btn)  # жмем финиш
    compl_text = get_text(driver, PageObject.SauceDemo.CartCheckout.complete_text)  # находим надпись
     # проверяем, что надпись состветствует
    assert compl_text == PageObject.SauceDemo.CartCheckout.complete_msg


def test_items_asc_sort_price(driver):
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    first_item = (list_items_price(driver))[0]  # находим первую цену
    click_element(driver, PageObject.SauceDemo.ShopPage.filter_btn)  # жмем на фильтр
    click_element(driver, PageObject.SauceDemo.ShopPage.filter_lohi)  # выбираем от меньшего к большему
    first_price = driver.find_element(*PageObject.SauceDemo.ShopPage.first_elem_price)
    price = first_price.text.replace("$", '').split('.')[0]
    assert int(first_item.split('.')[0]) > int(price)  # сверяем


def test_items_desc_sort_price(driver):
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    first_item = (list_items_price(driver))[0]  # находим первую цену
    click_element(driver, PageObject.SauceDemo.ShopPage.filter_btn)  # жмем на фильтр
    click_element(driver, PageObject.SauceDemo.ShopPage.filter_hilo)  # выбираем от большего к меньшему
    first_price = driver.find_element(*PageObject.SauceDemo.ShopPage.first_elem_price)
    price = first_price.text.replace("$", '').split('.')[0]
    assert int(first_item.split('.')[0]) < int(price)  # сверяем


def test_items_desc_sort_name(driver):
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    first_item = (list_items_names(driver))[0]  # находим первое имя
    click_element(driver, PageObject.SauceDemo.ShopPage.filter_btn)  # жмем на фильтр
    click_element(driver, PageObject.SauceDemo.ShopPage.filter_za)  # выбираем от большего к меньшему
    first_item_name = get_text(driver, PageObject.SauceDemo.ShopPage.first_elem_name)
    assert first_item.text != first_item_name  # сверяем имена


def test_items_asc_sort_name(driver):
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    click_element(driver, PageObject.SauceDemo.ShopPage.filter_za)  # выбираем от большего к меньшему
    first_item = (list_items_names(driver))[0]  # находим первое имя
    click_element(driver, PageObject.SauceDemo.ShopPage.filter_btn)  # жмем на фильтр
    click_element(driver, PageObject.SauceDemo.ShopPage.filter_btn)  # жмем на фильтр
    click_element(driver, PageObject.SauceDemo.ShopPage.filter_az)  # выбираем от меньшего к большему
    first_item_name = get_text(driver, PageObject.SauceDemo.ShopPage.first_elem_name)
    assert first_item.text != first_item_name  # сверяем


def test_about_btn(driver):
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    click_element(driver, PageObject.SauceDemo.ShopPage.menu_btn)  # жмем меню
    time.sleep(0.5)
    click_element(driver, PageObject.SauceDemo.ShopPage.about_btn)
    assert driver.current_url == url_from_about


def test_reset_button(driver):
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    add_to_cart(driver, PageObject.SauceDemo.ShopPage.backpack_add_to_cart_btn)  # добавляем в корзину
    # находим все кнопки ДОБАВИТЬ(их 5 шт, т.к. 1 товар в корзине добавлен)
    # считаем количество кнопок ДОБАВИТЬ
    count_before = get_length(driver, PageObject.SauceDemo.ShopPage.backpack_add_to_cart_btn)
    click_element(driver, PageObject.SauceDemo.ShopPage.menu_btn)  # находим кнопку меню, жмем ее
    time.sleep(0.5)
    click_element(driver, PageObject.SauceDemo.ShopPage.reset_btn)  # находим кнопку ресета, нажимаем на нее
    driver.refresh()  # обновляем страницу
    # находим все нопки добавить после ресета(их доожно быть 6, т.к. сделали сброс)
    count_after = get_length(driver, PageObject.SauceDemo.ShopPage.backpack_add_to_cart_btn)  # считаем их
    assert count_after > count_before  # сравниваем кол-во до и после


def test_logout(driver):
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    assert driver.current_url == url_shop  # проверяем что на странице магазина
    click_element(driver, PageObject.SauceDemo.ShopPage.menu_btn)  # находим кнопку меню, жмем ее
    time.sleep(0.5)
    click_element(driver, PageObject.SauceDemo.ShopPage.logout_btn)  # находим кнопку логаут, жмем ее
    assert driver.current_url == url  # проверяем что на странице авторизации
