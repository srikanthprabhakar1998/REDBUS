
import time
path = r'C:\Users\Sanjana_Jadhav\PycharmProjects\pythonProject\driver_name\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)
from selenium.webdriver.support.select import Select


file_path = r"http://190.210.184.180/login.do"
driver.get(file_path)
driver.maximize_window()


driver.find_element("xpath",'//input[@name="username"]').send_keys("abc@gmail.com")
time.sleep(1)

driver.find_element("xpath",'//input[@name="pwd"]').send_keys("12345")
time.sleep(1)