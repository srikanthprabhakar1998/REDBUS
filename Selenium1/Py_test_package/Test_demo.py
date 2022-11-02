# import re
# import pytest
#
# from selenium import webdriver
#
# @pytest.fixture()
# def init_driver():
#
#     path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
#     driver = webdriver.Chrome(executable_path=path)
#     driver.get(r"https://demowebshop.tricentis.com/")
#     driver.maximize_window()
#     yield driver
#     driver.close()
#
#
# class RegisterPage:
#
#     def __init__(self,driver):
#         self.driver = driver
#
#     def click_register_link(self):
#         self.driver.find_element("xpath", '//a[.="Register"]').click()
#
#     def click_male_gender(self):
#         self.driver.find_element("xpath", '//input[@id="gender-male"]').click()
#
#     def enter_firstname(self, fname):
#         self.driver.find_element("xpath", '//input[@id="FirstName"]').send_keys(fname)
#
#     def enter_lastname(self , lname):
#         self.driver.find_element("xpath", '//input[@id="LastName"]').send_keys(lname)
#
#     def enter_email(self , e_mail):
#         pattern = r"/W+@gmail\.com"
#         result = re.findall(pattern,e_mail)
#         self.driver.find_element("xpath", '//input[@id="Email"]').send_keys(e_mail)
#
#     def enter_pwd(self , p_wd):
#         assert len(p_wd) >= 6
#         self.driver.find_element("xpath", '//input[@id="Password"]').send_keys(p_wd)
#         return p_wd
#
#     def enter_cpwd(self ,c_pwd ,actual_pwd):
#         assert actual_pwd == c_pwd
#         self.driver.find_element("xpath", '//input[@id="ConfirmPassword"]').send_keys(c_pwd)
#
# class TestDemo:
#
#     def test_valid_pwd(self,init_driver):
#         driver = init_driver
#
#         obj = RegisterPage(driver)
#
#         obj.click_register_link()
#         obj.click_male_gender()
#         obj.enter_firstname("Brock")
#         obj.enter_lastname("beast")
#         obj.enter_email("Brockbeast@gmail.com")
#         actual_pwd = obj.enter_pwd("123456")
#         obj.enter_cpwd("123456", actual_pwd)
#
#     # @pytest.mark.skipif(4%2 == 0, reason= "okokok")
#     # @pytest.mark.invalid_TC
#     def test_invalid_pwd(self,init_driver):
#         obj = RegisterPage(init_driver)
#
#         obj.click_register_link()
#         obj.click_male_gender()
#         obj.enter_firstname("Brock")
#         obj.enter_lastname("beast")
#         obj.enter_email("Brockbeast@gmail.com")
#         actual_pwd = obj.enter_pwd("12345")
#         obj.enter_cpwd("1234566", actual_pwd)
#
#     # @pytest.mark.valid_TC
#     def test_valid_email(self,init_driver):
#
#         obj = RegisterPage(init_driver)
#
#         obj.click_register_link()
#         obj.click_male_gender()
#         obj.enter_firstname("Brock")
#         obj.enter_lastname("beast")
#         obj.enter_email("Brockbeast@gmail.com")
#         actual_pwd = obj.enter_pwd("123456")
#         obj.enter_cpwd("123456", actual_pwd)
#
#     # @pytest.mark.invalid_TC
#     def test_invalid_email(self,init_driver):
#         obj = RegisterPage(init_driver)
#
#         obj.click_register_link()
#         obj.click_male_gender()
#         obj.enter_firstname("Brock")
#         obj.enter_lastname("beast")
#         obj.enter_email("Brockbeast")
#         actual_pwd = obj.enter_pwd("123456")
#         obj.enter_cpwd("1234567", actual_pwd)
#
#     # @pytest.mark.valid_TC
#     def test_valid_cpwd(self,init_driver):
#
#         obj = RegisterPage(init_driver)
#
#         obj.click_register_link()
#         obj.click_male_gender()
#         obj.enter_firstname("Brock")
#         obj.enter_lastname("beast")
#         obj.enter_email("Brockbeast@gmail.com")
#         actual_pwd = obj.enter_pwd("123456")
#         obj.enter_cpwd("123456", actual_pwd)
#
#     # @pytest.mark.invalid_TC
#     def test_invalid_cpwd(self,init_driver):
#         obj = RegisterPage(init_driver)
#
#         obj.click_register_link()
#         obj.click_male_gender()
#         obj.enter_firstname("Brock")
#         obj.enter_lastname("beast")
#         obj.enter_email("Brockbeast@gmail.com")
#         actual_pwd = obj.enter_pwd("123456")
#         obj.enter_cpwd("1234567", actual_pwd)


#######################################################################################################################################################
import datetime
import re
from idlelib import browser

import pytest
import xlrd

from selenium import webdriver

@pytest.fixture(params=["Chrom","firefox","edge"])
def init_driver(request):
    browser = request.param

    if browser.lower() == "chrome":
        chrome_path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_path)
    elif browser.lower() == "firefox":
        firefow_path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\geckodriver.exe"
        driver = webdriver.Firefox(executable_path=firefow_path)
    else:
        edge_path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\msedgedriver.exe"
        driver = webdriver.Edge(executable_path=edge_path)



    driver.get(r"https://demowebshop.tricentis.com/")
    driver.maximize_window()
    yield driver
    driver.close()


class RegisterPage:

    def __init__(self,driver):
        self.driver = driver

    def click_register_link(self):
        self.driver.find_element("xpath", '//a[.="Register"]').click()

    def click_male_gender(self):
        self.driver.find_element("xpath", '//input[@id="gender-male"]').click()

    def enter_firstname(self, fname):
        self.driver.find_element("xpath", '//input[@id="FirstName"]').send_keys(fname)

    def enter_lastname(self , lname):
        self.driver.find_element("xpath", '//input[@id="LastName"]').send_keys(lname)

    def enter_email(self , e_mail):
        pattern = r"/W+@gmail\.com"
        result = re.findall(pattern,e_mail)
        self.driver.find_element("xpath", '//input[@id="Email"]').send_keys(e_mail)

    def enter_pwd(self , p_wd):
        assert len(p_wd) >= 6
        self.driver.find_element("xpath", '//input[@id="Password"]').send_keys(p_wd)
        return p_wd

    def enter_cpwd(self ,c_pwd ,actual_pwd):
        assert actual_pwd == c_pwd
        self.driver.find_element("xpath", '//input[@id="ConfirmPassword"]').send_keys(c_pwd)




data = [
     ("Tata","birla", "Tatabirla@gmail.com","123456", "123456"),
     ("Tata","birla", "Tatabirla@gmail.com","12345", "123456"),
     ("Tata","birla", "Tatabirla@gmail.com","123456", "123456"),
     ("Tata","birla", "Tatabirla@gmail.com","123456", "1234567"),
     ("Tata","birla", "Tatabirla@gmail.com","123456", "123456"),
     ("Tata","birla", "Tatabirla","123456", "123456")
       ]

class TestDemo:

    @pytest.mark.parametrize("f_name,l_name,email,pwd,c_pwd",data)
    def test_valid_pwd(self,f_name,l_name,email,pwd,c_pwd,init_driver):

        driver = init_driver
        try:

            obj = RegisterPage(driver)

            obj.click_register_link()
            obj.click_male_gender()
            obj.enter_firstname(f_name)
            obj.enter_lastname(l_name)
            obj.enter_email(email)
            actual_pwd = obj.enter_pwd(pwd)
            obj.enter_cpwd(c_pwd, actual_pwd)

        except AssertionError as error_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            path = r"C:\Users\srika\PycharmProjects\Selenium1\Py_test_package\Screenshot\\"
            driver.save_screenshot(path+name)
            raise error_msg



#####################################################################################################################################
# import re
# from idlelib import browser
## import pytest
#
# from selenium import webdriver
#
#
# @pytest.fixture(params=["Chrom", "firefox", "edge"])
# def init_driver(request):
#     browser = request.param
#
#     if browser.lower() == "chrome":
#         chrome_path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
#         driver = webdriver.Chrome(executable_path=chrome_path)
#     elif browser.lower() == "firefox":
#         firefow_path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\geckodriver.exe"
#         driver = webdriver.Firefox(executable_path=firefow_path)
#     else:
#         edge_path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\msedgedriver.exe"
#         driver = webdriver.Edge(executable_path=edge_path)
#
#     driver.get(r"https://demowebshop.tricentis.com/")
#     driver.maximize_window()
#     yield driver
#     driver.close()
#
#
# class RegisterPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def click_register_link(self):
#         self.driver.find_element("xpath", '//a[.="Register"]').click()
#
#     def click_male_gender(self):
#         self.driver.find_element("xpath", '//input[@id="gender-male"]').click()
#
#     def enter_firstname(self, fname):
#         self.driver.find_element("xpath", '//input[@id="FirstName"]').send_keys(fname)
#
#     def enter_lastname(self, lname):
#         self.driver.find_element("xpath", '//input[@id="LastName"]').send_keys(lname)
#
#     def enter_email(self, e_mail):
#         pattern = r"/W+@gmail\.com"
#         result = re.findall(pattern, e_mail)
#         self.driver.find_element("xpath", '//input[@id="Email"]').send_keys(e_mail)
#
#     def enter_pwd(self, p_wd):
#         assert len(p_wd) >= 6
#         self.driver.find_element("xpath", '//input[@id="Password"]').send_keys(p_wd)
#         return p_wd
#
#     def enter_cpwd(self, c_pwd, actual_pwd):
#         assert actual_pwd == c_pwd
#         self.driver.find_element("xpath", '//input[@id="ConfirmPassword"]').send_keys(c_pwd)
#
#
# class ReadExcel:
#     def read_testdata(self):
#         f_path = r"C:\Users\srika\PycharmProjects\Selenium1\test_data\Sriddd.xlsx"
#         wd = xlrd.open_workbook(f_path)
#         ws = wd.sheet_by_name("Demo1")
#         rows = ws.get_rows()
#         header = next(rows)
#         data = []
#         for row in rows:
#             element = (row[0].value, row[1].value, row[2].value, row[3].value, row[4].value)
#             data.append(element)
#             return data
#
#     def read_locator(self):
#         f_path = r"C:\Users\srika\PycharmProjects\Selenium1\test_data\~$locator.xlsx"
#         wd = xlrd.open_workbook(f_path)
#         ws = wd.sheet_by_name("Demo")
#         rows = ws.get_rows()
#         header = next(rows)
#         d = {}
#         for row in rows:
#             d[row[0].value] = (row[1].value , row[2].value)
#             return d
#
#
# class TestDemo:
#     read_xl = ReadExcel()
#     data = read_xl.read_testdata()
#
#     @pytest.mark.parametrize("f_name,l_name,email,pwd,c_pwd", data)
#     def test_valid_pwd(self, f_name, l_name, email, pwd, c_pwd, init_driver):
#         driver = init_driver
#         obj = RegisterPage(driver)
#
#         obj.click_register_link()
#         obj.click_male_gender()
#         obj.enter_firstname(f_name)
#         obj.enter_lastname(l_name)
#         obj.enter_email(email)
#         actual_pwd = obj.enter_pwd(pwd)
#         obj.enter_cpwd(c_pwd, actual_pwd)

######################################################################################################################################
# class RegisterPage:
#     """ consists of the automation script/ business logic of  Registration page of demo web shop"""
#     read_xl = ReadExcel()
#     reg_locators = read_xl.read_locators()
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def click_register_link(self):
#         locator = self.reg_locators["register_link"]
#         self.driver.find_element(*locator).click()
#
#     def select_female_radio_btn(self):
#         locator_name, locator_value = self.reg_locators["female_radio_btn"]
#         self.driver.find_element(locator_name, locator_value).click()
#
#     def select_male_radio_btn(self):
#         locator = self.reg_locators["male_radio_btn"]
#         self.driver.find_element(*locator).click()
#
#     def enter_firstname(self, f_name):
#         locator = self.reg_locators["firstname_txt"]
#         self.driver.find_element(*locator).send_keys(f_name)
#
#     def enter_lastname(self, l_name):
#         locator = self.reg_locators["lastname_txt"]
#         self.driver.find_element(*locator).send_keys(l_name)
#
#     def enter_email(self, email):
#         pattern = r"\w+@gmail\.com"
#         result = re.findall(pattern, email)
#         assert result, "invalid email"
#
#         locator = self.reg_locators["email_txt"]
#         self.driver.find_element(*locator).send_keys(email)
#
#     def enter_password(self, pwd):
#         if isinstance(pwd, float):
#             pwd = str(int(pwd))
#
#         assert len(pwd) >= 6, "password should have atleast 6 characters"
#         locator = self.reg_locators["password_txt"]
#         self.driver.find_element(*locator).send_keys(pwd)
#         return pwd
#
#     def confirm_password(self, c_pwd, actual_pwd):
#         if isinstance(c_pwd, float):
#             c_pwd = str(int(c_pwd))
#
#         locator = self.reg_locators["confirm_password_txt"]
#         assert actual_pwd == c_pwd, "passwords are different"
#         self.driver.find_element(*locator).send_keys(c_pwd)[]