from selenium.webdriver.common.by import By


# Define locators for the elements on the login locators
class LoginPageLocators:
    USERNAME = (By.NAME, "user-name")  # Locator for the username field
    PASSWORD = (By.NAME, "password")  # Locator for the password field
    LOGIN_BUTTON = (By.ID, "login-button")  # Locator for the login button
    SUCCESS_INDICATOR = (By.ID, '"accountPag')  # Locator for the success indicator


# Define locators for the elements on the add to cart locators
class AddToCartLocators:
    CLICK_PRODUCT_LINK = (By.XPATH, "//a[text()='Product']")  # Locator for the product link
    CLICK_PRODUCT_LINK_BUTTON = (By.ID, 'addToCart')  # Locator for the product link button
    CLICK_ADD_TO_CART_ICON = (By.ID, "cartIcon")  # Locator for the add to cart icon
    CART_ITEM = (By.XPATH, '//xpath_to_cart_item')  # Locator for the cart item
