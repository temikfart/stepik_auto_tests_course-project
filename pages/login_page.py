from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "url isn't correct for login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is missing"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is missing"

    def register_new_user(self, email, password):
        self.should_be_login_page()

        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        input_email.send_keys(email)

        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        input_password.send_keys(password)

        input_confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        input_confirm_password.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

