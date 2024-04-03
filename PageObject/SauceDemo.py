from selenium.webdriver.common.by import By


class LoginPage:
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")
    logo_text = (By.CLASS_NAME, "app_logo")
    error_msg = (By.TAG_NAME, "h3")
    err_msg_text = "Epic sadface: Username and password do not match any user in this service"


class ShopPage:
    backpack_item = (By.CLASS_NAME, "inventory_item_name")
    backpack_add_to_cart_btn = (By.XPATH, "//*[text()='Add to cart']")
    cart_btn = (By.CLASS_NAME, "shopping_cart_link")
    item_in_cart = (By.CLASS_NAME, "inventory_details_name large_size")
    remove_btn = (By.XPATH, "//*[text()='Remove']")
    item_in_shop = (By.XPATH, "//*[text()='locator']")
    item_img = (By.XPATH, "//img[@alt='locator']")
    filter_btn = (By.CLASS_NAME, "select_container")
    filter_az = (By.XPATH, "//*[@value='az']")
    filter_za = (By.XPATH, "//*[@value='za']")
    filter_lohi = (By.XPATH, "//*[@value='lohi']")
    filter_hilo = (By.XPATH, "//*[@value='hilo']")
    first_elem_price = (By.XPATH, '(//*[@class="inventory_item_price"])[1]')
    first_elem_name = (By.CLASS_NAME, 'inventory_item_name')


class ItemDescription:
    item_name = (By.CLASS_NAME, "inventory_details_name large_size")
    add_btn = (By.ID, "add-to-cart")
    description = (By.CLASS_NAME, "inventory_details_desc_container")


class CartCheckout:
    checkout_btn = (By.ID, "checkout")
    first_n = (By.ID, "first-name")
    last_n = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    finish_btn = (By.ID, "finish")
    complete_text = (By.CLASS_NAME, "complete-header")
    complete_msg = "Thank you for your order!"


