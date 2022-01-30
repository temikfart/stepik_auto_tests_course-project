from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a")


class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:first-child")
    NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:first-child strong")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_COST = (By.CSS_SELECTOR, "div.product_main p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert-info strong")
