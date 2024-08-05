import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Config.configs import Config
from loginPage.login_page_test import LoginPage, AddToCartPage


# @pytest.fixture(scope="module")
# def driver_setup():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Run Chrome in headless mode
#     chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.implicitly_wait(20)
#     driver.maximize_window()
#     yield driver
#     driver.quit()


# Fixture to set up the WebDriver
@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()  # Initialize the Chrome WebDriver
    driver.implicitly_wait(20)  # Set an implicit wait of 20 seconds
    driver.maximize_window()  # Maximize the browser window
    yield driver  # Provide the driver instance to the tests
    driver.quit()  # Quit the driver after the tests are done


# Fixture to log in to the website
@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup  # Use the driver setup fixture
    login_page = LoginPage(driver)  # Initialize the LoginPage with the driver
    login_page.login_url(Config.BASE_URL)  # Navigate to the login URL
    return login_page  # Provide the login page instance to the tests


# Test to verify the login functionality on the e-commerce website
def test_login_page_on_ecommerce_website(login):
    login.enter_username(Config.USERNAME)  # Enter the username
    login.enter_password(Config.PASSWORD)  # Enter the password
    login.click_login_button()  # Click the login button
    login.assert_successful_login()  # Assert that the login was successful


# Test to verify the add-to-cart functionality on the e-commerce website
def test_order_product_on_ecommerce_website(login):
    add_to_cart_page = AddToCartPage(login.driver)  # Initialize the AddToCartPage with the driver
    add_to_cart_page.navigate_to_product()  # Navigate to the product
    add_to_cart_page.click_product_link_button()  # Click the product link button
    add_to_cart_page.click_add_to_cart_icon()  # Click the add to cart icon
    add_to_cart_page.assert_item_added_to_cart()  # Assert that the item was added to the cart
