import pytest
from POM.login_page import LoginPage
from Library.excel_lib import ReadExcel
from Library.config import Configuration


class TestLoginPage:
    read_xl = ReadExcel()
    data = read_xl.read_testdata(Configuration.LOGIN_TESTDATA_SHEET)

    @pytest.mark.parametrize("email,pwd", data)
    def test_login(self, init_driver, email, pwd):
        driver = init_driver
        lp = LoginPage(driver)
        lp.click_login_link()
        lp.enter_email(email)
        lp.enter_password(pwd)
