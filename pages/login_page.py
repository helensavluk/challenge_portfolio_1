from selenium.webdriver.chrome.webdriver import WebDriver
from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    remind_password_button_xpath = "//*[text()='Remind password']"
    language_select_area_xpath = "//*[@class='MuiSelect-nativeInput']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_in_button(self, button):
        return self.driver.find_element(sign_in_button_xpath, button).click()
