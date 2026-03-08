import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        URL = self.browser.current_url
        assert ("selenium1py.pythonanywhere.com" in URL
                and "/accounts/login/" in URL), "Not open login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not present"

    def register_new_user(self, email = None, password = None):
        if email is None:
            email = str(time.time()) + "@fakemail.com"

        if password is None:
            password = str(time.time()) + "password"

        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_input.send_keys(password)
        password_confirm_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        password_confirm_input.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
