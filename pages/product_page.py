from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        # self.solve_quiz_and_get_code()
        self.should_be_success_message()
        self.should_be_same_products_in_basket_and_on_the_page()
        self.should_be_correct_price_in_basket()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "'Add to basket' button is missing"

    def should_not_be_present_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.NAME_IN_SUCCESS_MESSAGE), \
            "'Added to basket' success message is missing"

    def should_be_same_products_in_basket_and_on_the_page(self):
        name_of_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        name_of_added_product = self.browser.find_element(*ProductPageLocators.NAME_IN_SUCCESS_MESSAGE).text
        assert name_of_product == name_of_added_product, \
            "name of product and of the added to basket product are not same"

    def should_be_correct_price_in_basket(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_cost == basket_price, \
            "product cost and basket price are not same"
