# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# from selenium import webdriver
#
# path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get(r'https://demo.actitime.com/login.do')
# driver.maximize_window()
#
#
# class Login_page:
#
#     def enter_user_name(self, user_):
#         assert user_ == "admin"
#         driver.find_element("xpath", '//input[@id="username"]').send_keys(user_)
#
#
#     def enter_password(self, pwd):
#         assert pwd == "manager"
#         driver.find_element("xpath", '//input[@placeholder="Password"]').send_keys(pwd)
#
#
#     def click_submitt(self):
#         driver.find_element("xpath", '//div[.="Login "]').click()
#         wait_ = WebDriverWait(driver,20)
#         wait_.until(expected_conditions.title_is())
#
#     def click_logout(self):
#         driver.find_element("xpath", '//a[@id="logoutLink"]').click()+
#
# class TestLoginPage:
#
#     def test_vaild_user_name(self):
#         obj = Login_page()
#         obj.enter_user_name("admin")
#         obj.enter_password("manager")
#         obj.click_submitt()
#         time.sleep(2)
#         obj.click_logout()
import pytest


def test_invaild_user_name(self):
        obj = Login_page()
        obj.enter_user_name("adminm")
        obj.enter_password("manager")
        obj.click_submitt()


#####################################################################################################################################
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium import webdriver

path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get(r'https://demo.actitime.com/login.do')
driver.maximize_window()



class Login_page:
    def __init__(self,driver):
        self.driver

    def enter_user_name(self, user_):
        assert user_ == "admin"
        driver.find_element("xpath", '//input[@id="username"]').send_keys(user_)


    def enter_password(self, pwd):
        assert pwd == "manager"
        driver.find_element("xpath", '//input[@placeholder="Password"]').send_keys(pwd)


    def click_submitt(self):
        driver.find_element("xpath", '//div[.="Login "]').click()
        wait_ = WebDriverWait(driver,20)
        wait_.until(expected_conditions.title_is())

    def click_logout(self):
        driver.find_element("xpath", '//a[@id="logoutLink"]').click()

data = [
    ("admin","manager"),
    ("adminn","manager"),
    ("admin","manager"),
    ("admin","managere")
]

class TestLoginPage:
    @pytest.mark.parametrize("use_nam","pwd",data)
    def test_vaild_user_name(self,use_nam,pwd,init_driver):

        driver = init_driver
        obj = TestLoginPage(driver)
        obj = Login_page()
        obj.enter_user_name(use_nam)
        obj.enter_password(pwd)
        obj.click_submitt()
        time.sleep(2)
        obj.click_logout()














































































































































































    def test_vaild_password(self):
        obj = Login_page()
        obj.enter_user_name("admin")
        obj.enter_password("manager")
        obj.click_submitt()
        time.sleep(2)
        obj.click_logout()


    def test_invaild_password(self):
        obj = Login_page()
        obj.enter_user_name("admin")
        obj.enter_password("managerr")
        obj.click_submitt()
