import os
import unittest

from selenium import webdriver

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def Test_log_into_the_system(self:
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com') \
        user_login.type_in_password('Test-1234')\
        user_login.click_sign_in_button()

    @classmethod
    def tearDown(self):
        self.driver.quit()
