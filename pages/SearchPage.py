
from pages.BasePage import BasePage


class Searchpage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    valid_product_link_text = "iMac"
    no_product_message_xpath = "//*[@id='button-search']/following-sibling::p"


    def display_status_of_product(self):
        return self.check_display_status_of_element("valid_product_link_text", self.valid_product_link_text)


    def retrieve_no_product_message(self):
        return self.retrieve_element_text("no_product_message_xpath", self.no_product_message_xpath)
