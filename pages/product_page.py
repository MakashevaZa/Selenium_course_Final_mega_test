from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Button Add-to-cart is not presented"
        
    def add_to_cart(self):
        add_product_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_product_button.click() 
        
    def should_have_message_the_very_product_was_added(self):
        element1 = self.get_text_value(*ProductPageLocators.PRODUCT_NAME)
        element2 = self.get_text_value(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_ON_ADDING)
        assert element1 == element2, "Product names differ"
    
    def should_have_message_with_cart_having_same_price(self):
        element1 = self.get_text_value(*ProductPageLocators.PRODUCT_PRICE)
        element2 = self.get_text_value(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE_ON_NEW_CART_PRICE)
        assert element1 == element2, "Prices differ"

    def should_disappear_success_message(self):
        assert self.disappeared(*ProductPageLocators.SUCCESS_MESSAGE_ON_ADDING_TO_CART, 4), "The success message of adding a product element doesn't disappear"

    def should_not_have_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ON_ADDING_TO_CART, 4), "The success message of adding a product to cart appeared"

