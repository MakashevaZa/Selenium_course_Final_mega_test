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
        assert element1 == element2, "Product name differ"    
    
    def should_have_message_with_cart_having_same_price(self):
        element1 = self.get_text_value(*ProductPageLocators.PRODUCT_PRICE)
        element2 = self.get_text_value(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE_ON_NEW_CART_PRICE)
        assert element1 == element2, "Prices differ"
        