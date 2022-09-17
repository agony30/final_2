from .base_page import BasePage
from .locators import LoginPageLocators, RegPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "The page does not contain the word 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email: str, password: str):
        email_input = self.browser.find_element(*RegPageLocators.EMAIL_REG)
        email_input.send_keys(email)
        pass1_input = self.browser.find_element(*RegPageLocators.PASSWORD1_REG)
        pass1_input.send_keys(password)
        pass2_input = self.browser.find_element(*RegPageLocators.PASSWORD2_REG)
        pass2_input.send_keys(password)
        confirm_btn = self.browser.find_element(*RegPageLocators.REGISTER_BTN)
        confirm_btn.click()
