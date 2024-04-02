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
    wait_page_open(driver)  # ждем открытия страницы
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    add_to_cart(driver, PageObject.SauceDemo.ShopPage.backpack_add_to_cart_btn)  # добавляем в корзину
    go_to_cart(driver)  # переходим в корзину
    item = driver.find_element(*PageObject.SauceDemo.ShopPage.item_in_cart)
    assert item.text == "Sauce Labs Backpack"  # сверяем, что товар в корзине


def test_delete_item_from_cart(driver):
    wait_page_open(driver)  # ждем открытия страницы
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
    wait_page_open(driver)  # ждем открытия страницы
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    item = find_item_by_name(driver, "Sauce Labs Backpack")  # находим товар
    item.click()  # открываем его
    add_to_cart(driver, PageObject.SauceDemo.ItemDescription.add_btn)  # добавляем в корзину
    name = find_item_by_name(driver, "Sauce Labs Backpack")  # находим имя
    assert name.text == "Sauce Labs Backpack"  # сверяем, что оно верное


def test_delete_item_from_description(driver):
    wait_page_open(driver)  # ждем открытия страницы
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    item = find_item_by_name(driver, "Sauce Labs Backpack")  # находим товар по имени
    item.click()  # открываем его
    add_to_cart(driver, PageObject.SauceDemo.ItemDescription.add_btn)  # добавляем в корзину
    delete_item(driver)  # удаляем его


def test_item_description_by_name(driver):
    wait_page_open(driver)  # ждем открытия страницы
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    item = find_item_by_name(driver, "Sauce Labs Backpack")  # находим товар по имени
    item.click()  # открываем его
    description = driver.find_element(*PageObject.SauceDemo.ItemDescription.description)
    assert description  # сверяем, что элемент описания товара есть на странице


def test_item_description_by_image(driver):
    wait_page_open(driver)  # ждем открытия страницы
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    item = find_item_by_img_name(driver, "Sauce Labs Backpack")  # находим товар по имени картинки
    item.click()  # открываем его
    description = driver.find_element(*PageObject.SauceDemo.ItemDescription.description)
    assert description  # сверяем, что элемент описания товара есть на странице


def test_purchase_complete(driver):
    wait_page_open(driver)  # ждем открытия страницы
    login_method(driver, correct_login, correct_password)  # вводим логин, пароль, логинимся
    add_to_cart(driver, PageObject.SauceDemo.ShopPage.backpack_add_to_cart_btn)  # добавляем в корзину
    go_to_cart(driver)  # переходим в корзину
    checkout_btn = driver.find_element(*PageObject.SauceDemo.CartCheckout.checkout_btn)
    checkout_btn.click()  # жмем кнопку в чекаут
    enter_text(driver, PageObject.SauceDemo.CartCheckout.first_n, first_name)  # вводим имя
    enter_text(driver, PageObject.SauceDemo.CartCheckout.last_n, last_name)  # вводим фамилию
    enter_text(driver, PageObject.SauceDemo.CartCheckout.postal_code, zip_code)  # вводим индекс
    continue_btn = driver.find_element(*PageObject.SauceDemo.CartCheckout.continue_btn)
    continue_btn.click()  # жмем далее
    finish_btn = driver.find_element(*PageObject.SauceDemo.CartCheckout.finish_btn)
    finish_btn.click()  # жмем финиш
    compl_text = driver.find_element(*PageObject.SauceDemo.CartCheckout.complete_text)  # находим надпись
     # проверяем, что надпись состветствует
    assert compl_text.text == PageObject.SauceDemo.CartCheckout.complete_msg


def test_items_desc_sort_price(driver):
    wait_page_open(driver)  # ждем открытия страницы
    enter_login(driver, correct_login)  # вводим логин
    enter_password(driver, correct_password)  # вводим пароль
    click_submit(driver)  # логинимся
    first_item = (list_items_price(driver))[0]




