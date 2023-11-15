from datetime import datetime
from pages.HomePage import Homepage


import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class Testlogin:

    def test_login_with_valid_credentials(self):
        home_page = Homepage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page = home_page.select_login_option()
        account_page = login_page.login_to_application("srikanth.srikanthsreesanth@gmail.com", "123456")
        assert account_page.display_status_of_edit_your_account_information_option()


    def test_login_with_invalid_email_and_valid_password(self):
        home_page = Homepage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page = home_page.select_login_option()
        login_page.login_to_application(self.generate_email_with_time_stamp(), "123456")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)




    def test_login_with_valid_email_and_invalid_password(self):
        home_page = Homepage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page = home_page.select_login_option()
        login_page.login_to_application("srikanth.srikanthsreesanth@gmail.com", "123456789")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)


    def test_login_without_entering_credentials(self):
        home_page = Homepage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page = home_page.select_login_option()
        login_page.login_to_application("", "")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)


    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "srikanth" + time_stamp + "@gmail.com"