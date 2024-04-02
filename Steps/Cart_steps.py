from selenium.webdriver.common.by import By

import PageObject.SauceDemo


def add_to_cart(driver, locator):
    item = driver.find_element(*locator)
    item.click()


def go_to_cart(driver):
    cart = driver.find_element(*PageObject.SauceDemo.ShopPage.cart_btn)
    cart.click()


def delete_item(driver):
    item = driver.find_element(*PageObject.SauceDemo.ShopPage.remove_btn)
    item.click()
