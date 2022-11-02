import datetime

import pytest
from Library.excel_lib import ReadExcel
from POM.register_page import RegisterPage
from Library.config import Configuration


class TestRegisterPage:


    read_xl = ReadExcel()
    data = read_xl.read_testdata()


    @pytest.mark.parametrize("f_name,l_name",data)
    def test_valid_pwd(self,f_name,l_name,init_driver):

        driver = init_driver
        try:

            obj = RegisterPage(driver)

            obj.click_register_link()
            obj.select_male_radio_btn()
            obj.enter_firstname(f_name)
            obj.enter_lastname(l_name)
            obj.enter_email(email)
            actual_pwd = obj.enter_password(pwd)
            obj.confirm_password(c_pwd, actual_pwd)

        except BaseException as error_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Configuration.SCREENSHOT_PATH + name)
            raise error_msg