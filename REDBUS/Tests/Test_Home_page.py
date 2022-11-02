import datetime

import pytest
from library.excel_lib import ReadExcel
from POM.home_page import HomePage
from library.config import Configuration


class TestHomePage:
    read_xl = ReadExcel()
    data = read_xl.read_testdata(Configuration.RED_TESTDATA_SHEET)

    @pytest.mark.parametrize("f_name,l_name", data)
    def test_click_Show_my_ticket(self, f_name, l_name, init_driver):

        driver = init_driver
        try:

            obj = HomePage(driver)
            obj.click_Manager_Booking()
            obj.select_Show_my_ticket()
            obj.enter_From_textfield(f_name)
            obj.enter_To_textfield(l_name)
            obj.click_submit()


        except BaseException as error_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Configuration.SCREENSHOT_PATH+name)
            raise error_msg
