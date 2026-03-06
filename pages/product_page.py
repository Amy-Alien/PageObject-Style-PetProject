from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_product_name_in_success_message(self.get_product_name())
        self.should_be_price_in_basket_equal_product_price(self.get_product_price())

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_product_name_in_success_message(self, product_name):
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text
        assert product_name == product_name_in_message, "Product name in success message does not match the actual product name"

    def should_be_price_in_basket_equal_product_price(self, product_price):
        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET_TOTAL_MESSAGE).text
        assert product_price == price_in_message, "Product price in basket total message does not match the actual product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message not be present"

    def should_disappear_of_success_message(self):
        if len(self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE)) > 0:
            assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Message is not disappeared"
        assert False, "Success message is not present"