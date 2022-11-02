import re
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from library.excel_lib import ReadExcel
from library.config import Configuration


class HomePage:
    """ consists of the automation script/ business logic of  Registration page of demo web shop"""
    read_xl = ReadExcel()
    reg_locators = read_xl.read_locator(Configuration.RED_LOCATOR_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def click_Manager_Booking(self):
        locator = self.reg_locators["Manager_Booking"]
        self.driver.find_element(*locator).click()

    def select_Show_my_ticket(self):
        locator_name, locator_value = self.reg_locators["Show_my_ticket"]
        self.driver.find_element(locator_name, locator_value).click()

    def enter_From_textfield(self, f_name):
        locator = self.reg_locators["From_textfield"]
        self.driver.find_element(*locator).send_keys(f_name)
        time.sleep(1)

    def enter_To_textfield(self, l_name):
        if isinstance(l_name, float):
            l_name = int(l_name)
        # assert isinstance(l_name, int)
        locator = self.reg_locators["To_textfield"]
        self.driver.find_element(*locator).send_keys(l_name)
        time.sleep(10)

    def click_submit(self):
        locator = self.reg_locators["Submit_button"]
        self.driver.find_element(*locator).click()
        wait_ = WebDriverWait(self.driver, 15)
        assert wait_.until(expected_conditions.title_contains("redBus revamp"))

        # actual_result = "redBus revamp"
        # result = self.driver.title()
        # assert result
