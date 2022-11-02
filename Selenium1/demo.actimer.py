from  selenium import webdriver
import time
path =r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
driver= webdriver.Chrome(executable_path= path)
driver.get("https://demowebshop.tricentis.com/")
# driver.find_element("id","username").send_keys("admin")
# driver.find_element("class name", "textField.pwdfield").send_keys("manager")
# driver.find_element("id","loginButton").click()


#by using css selector
driver.find_element("css selector",'a[class="ico-register"]').click()
driver.find_element("css selector",'input[id="gender-male"]').click()
driver.find_element("css selector",'[id="FirstName"]').send_keys("srikanth")
driver.find_element("css selector", '[id="LastName"]').send_keys("P")
time.sleep(2)
driver.find_element("css selector",'input[id="Email"]').send_keys("srikanthprabhakar855@gmail.com")
driver.find_element("css selector",'input[id="Password"]').send_keys("srikky@123")
time.sleep(2)
driver.find_element("css selector",'input[id="ConfirmPassword"]').send_keys("srikky@123")
driver.find_element("css selector",'input[id= "register-button"]').click()
time.sleep(2)
driver.find_element("css selector",'input[class name= "button-1 register-continue-button"]').click()