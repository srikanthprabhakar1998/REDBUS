import pytest

from Library.excle_lib import ReadExcle
from POM.friends_module import FriendsPage
from Library.config import Configuration


class TestFriendsPage:
    obj = ReadExcle()
    data = obj.read_test_data(Configuration.FRIENDS_TEST_DATASHEET)

    @pytest.mark.parametrize("email, pwd", data)
    def test_click_login_link(self, init_driver, email, pwd):
        driver = init_driver
        lp = FriendsPage(driver)
        lp.user_name(email)
        lp.password_1(pwd)
        lp.login_1()
        lp.TC_Home_001()

        # lp.TC_Home_002()

        # lp.TC_HOME_003()
        # lp.TC_HOME_004()
        lp.TC_HOME_005()
        # lp.TC_HOME_006()


        # lp.TC_HOME_011()
        # lp.TC_HOME_012()
        lp.TC_HOME_013()

        lp.TC_HOME_014()
        # lp.TC_HOME_015()

        # lp.TC_HOME_016()
        # lp.TC_HOME_017()
        #         lp.TC_HOME_018()
        # lp.TC_HOME_019()
        # lp.TC_HOME_020()
        #                     lp.TC_HOME_021()
        # lp.TC_HOME_022()
        # lp.TC_HOME_023()

        # lp.TC_HOME_024()
        # lp.TC_HOME_025()

        # lp.TC_HOME_026()
        # lp.TC_HOME_027()
        # lp.TC_HOME_028()
        # lp.TC_HOME_029()

        # lp.TC_HOME_030()
        # lp.TC_HOME_031()
