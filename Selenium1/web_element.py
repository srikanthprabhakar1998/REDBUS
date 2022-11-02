import time

from selenium import webdriver
path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
driver =webdriver.Chrome(executable_path=path)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
# element = driver.find_element("id", "small-searchterms")
# print(element)
# time.sleep(2)
# element.click()
# time.sleep(2)
# element.send_keys("mobiles")
driver.find_element("class name", "ico-register").click()
driver.find_element("id", "gender-male").click()
time.sleep(2)
driver.find_element("id","FirstName").send_keys("Srikanth")
driver.find_element("id", "LastName").send_keys("P")
time.sleep(2)
driver.find_element("id", "Email").send_keys("srikanthprabhakar855@gmail.com")
driver.find_element("id", "Password").send_keys("srikky@123")
time.sleep(2)
driver.find_element("id","ConfirmPassword").send_keys("srikky@123")
driver.find_element("id", "register-button").click()
time.sleep(2)
driver.find_element("class name", "button-1 register-continue-button").click()



#locating using clss name
# element = driver.find_element("class" , "ytd-searchbox")
# element.click()
# element.send_keys("Pushpa songs")