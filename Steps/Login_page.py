import time

import pytest

from Steps.Shop_steps import enter_text
from credentials import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import PageObject.SauceDemo


@pytest.fixture
def driver():
    # Инициализация WebDriver
    driver = webdriver.Chrome()
    yield driver

    # Закрытие браузера после выполнения тестов
    driver.quit()


def wait_page_open(driver):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))


def click_submit(driver):
    submit_button = driver.find_element(*PageObject.SauceDemo.LoginPage.login_button)
    submit_button.click()


def login_method(driver, login, pwd):
    wait_page_open(driver)  # ждем открытия страницы
    enter_text(driver, PageObject.SauceDemo.LoginPage.username_field, login)
    enter_text(driver, PageObject.SauceDemo.LoginPage.password_field, pwd)
    click_submit(driver)

