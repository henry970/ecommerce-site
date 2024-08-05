import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from LoginPageLocators.Login_page_locators import LoginPageLocators, AddToCartLocators


class LoginPage:
    def __init__(self, driver):
        # Initialize the driver
        self.driver = driver

    def login_url(self, url):
        # Navigate to the login URL
        self.driver.get(url)

    def enter_username(self, username):
        # Wait until the username field is present
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.USERNAME))
        # Check if the username field is active
        if enter_username.is_enabled():
            # Enter the username
            enter_username.send_keys(username)
        else:
            # Take a screenshot if the username field is not active
            self.take_screenshot("username_not_active")
            raise Exception("Username field is not active")

    def enter_password(self, password):
        # Wait until the password field is present
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.PASSWORD))
        # Check if the password field is active
        if enter_password.is_enabled():
            # Enter the password
            enter_password.send_keys(password)
        else:
            # Take a screenshot if the password field is not active
            self.take_screenshot("password_not_active")
            raise Exception("Password field is not active")

    def click_login_button(self):
        # Wait until the login button is present
        click_login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        # Check if the login button is active
        if click_login_button.is_enabled():
            # Click the login button
            click_login_button.click()
        else:
            # Take a screenshot if the login button is not active
            self.take_screenshot("login_button_not_active")
            raise Exception("Login button is not active")

    def take_screenshot(self, name):
        # Take a screenshot and save it with the provided name
        self.driver.save_screenshot(f"{name}.png")

    def assert_successful_login(self):
        # Wait until the success indicator is present
        success_indicator = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginPageLocators.SUCCESS_INDICATOR))
        # Assert that the success indicator is displayed
        assert success_indicator.is_displayed(), "Login was not successful"


# Define locators for the elements on the add-to-cart page
class AddToCartPage:
    def __init__(self, driver):
        # Initialize the driver
        self.driver = driver

    def navigate_to_product(self):
        # Wait until the product link is present and click it
        product_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.CLICK_PRODUCT_LINK))
        product_link.click()

    def click_product_link_button(self):
        # Wait until the product link button is present and click it
        product_link_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.CLICK_PRODUCT_LINK_BUTTON))
        product_link_button.click()

    def click_add_to_cart_icon(self):
        # Wait until the add to cart icon is present and click it
        add_to_cart_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.CLICK_ADD_TO_CART_ICON))
        if add_to_cart_icon.is_enabled():
            add_to_cart_icon.click()
        else:
            # Take a screenshot if the add to cart icon is not active
            self.take_screenshot("add_to_cart_icon_not_active")
            raise Exception("Add to cart icon is not active")

    def take_screenshot(self, name):
        # Take a screenshot and save it with the provided name
        self.driver.save_screenshot(f"{name}.png")

    def assert_item_added_to_cart(self):
        # Wait until the cart item is present
        cart_item = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.CART_ITEM))
        # Assert that the cart item is displayed
        assert cart_item.is_displayed(), "Item was not added to the cart"
