from selenium.webdriver.chrome.webdriver import WebDriver
from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    remind_password_button_xpath = "//*[text()='Remind password']"
    language_select_area_xpath = "//*[@class='MuiSelect-nativeInput']"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_title = "Scouts panel - sign in"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_in_button(self, button):
        return self.driver.find_element(self.sign_in_button_xpath, button)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title
