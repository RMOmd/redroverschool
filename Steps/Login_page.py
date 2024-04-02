import pytest
from selenium.webdriver.common.by import By
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
    driver.get('https://www.saucedemo.com/')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))


def enter_login(driver, login):
    login_field = driver.find_element(*PageObject.SauceDemo.LoginPage.username_field)
    login_field.send_keys(login)


def enter_password(driver, pwd):
    pass_field = driver.find_element(*PageObject.SauceDemo.LoginPage.password_field)
    pass_field.send_keys(pwd)


def click_submit(driver):
    submit_button = driver.find_element(*PageObject.SauceDemo.LoginPage.login_button)
    submit_button.click()
