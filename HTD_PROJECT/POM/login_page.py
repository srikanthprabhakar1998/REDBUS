import re
from Library.excel_lib import ReadExcel
from Library.config import Configuration


class LoginPage:

    read_xl = ReadExcel()
    login_locators = read_xl.read_locator(Configuration.LOGIN_LOCATOR_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def click_login_link(self):
        locator = self.login_locators["login_link"]
        self.driver.find_element(*locator).click()

    def enter_email(self,email):
        locator = self.login_locators["Email"]
        self.driver.find_element(*locator).send_keys(email)

    def enter_password(self,pwd):
        locator = self.login_locators["password"]
        self.driver.find_element(*locator).send_keys(pwd)

    def click_login_button(self):
        locator = self.login_locators["Login"]
        self.driver.find_element(*locator).click()
