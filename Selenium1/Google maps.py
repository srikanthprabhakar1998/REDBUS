import time

from selenium import webdriver
path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
driver=webdriver.Chrome(executable_path=path)
driver.get("https://www.google.com/maps/@12.9978608,77.5275458,15z")
driver.find_element("id","searchboxinput").send_keys("bangalore")
time.sleep(2)
driver.find_element("id","hArJGc").click()
time.sleep(2)
driver.find_element("xpath",'//input[@placeholder="Choose starting point, or click on the map..."]').send_keys("mysore")
driver.find_element("class name","mL3xi").click()