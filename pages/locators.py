from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    
class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_IN_MESSAGE_ON_ADDING = (By.CSS_SELECTOR, "#messages > div.alert-success:nth-child(1) div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE_IN_MESSAGE_ON_NEW_CART_PRICE = (By.CSS_SELECTOR, "#messages > div.alert-info div.alertinner p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    SUCCESS_MESSAGE_ON_ADDING_TO_CART = (By.CSS_SELECTOR, "div.alert-success")
