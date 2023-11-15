

from pages.BasePage import BasePage
from pages.AccountPage import Accountpage



class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_address_field_name = "email"
    password_field_name = "password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_email_address(self, email_address_text):
        self.type_into_element(email_address_text, "email_address_field_name", self.email_address_field_name)


    def enter_password(self, password_text):
        self.type_into_element(password_text, "password_field_name", self.password_field_name)


    def click_on_login_button(self):
        self.element_click("login_button_xpath", self.login_button_xpath)
        return Accountpage(self.driver)


    def login_to_application(self, email_address_text, password_text):
        self.enter_email_address(email_address_text)
        self.enter_password(password_text)
        return self.click_on_login_button()


    def retrieve_warning_message(self):
        return self.retrieve_element_text("warning_message_xpath", self.warning_message_xpath)