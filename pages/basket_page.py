from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text
        assert "basket is empty" in empty_message, "basket is not empty"

    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "url is not correct for basket page"
