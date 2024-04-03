from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import PageObject.SauceDemo


def find_item_by_name(driver, item_name):
    loc = PageObject.SauceDemo.ShopPage.item_in_shop[1]
    locator_edited = loc.replace("locator", item_name)
    item = driver.find_element(By.XPATH, locator_edited)
    return item


def find_item_by_img_name(driver, img_name):
    image = PageObject.SauceDemo.ShopPage.item_img[1]
    locator_edited = image.replace("locator", img_name)
    item = driver.find_element(By.XPATH, locator_edited)
    return item


def enter_text(driver, locator, text):
    find_field = driver.find_element(*locator)
    find_field.send_keys(text)


def list_items_price(driver):
    items = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    items_price = []
    for item in items:
        price_item = item.text.replace("$", '')
        items_price.append(price_item)

    return items_price


def list_items_names(driver):
    items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    items_name = []
    for item in items:
        # price_item = item.text.replace("$", '')
        items_name.append(item)
    return items_name
