from selenium import webdriver
path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
driver =webdriver.Chrome(executable_path=path)
driver.get(r"https://demowebshop.tricentis.com/")

driver.find_element("xpath",'//a[@class="ico-register"]').click()
driver.find_element("xpath",'//input[@id="gender-male"]').click()
driver.find_element("xpath",'//input[@id="FirstName"]').send_keys("srikky")
driver.find_element("xpath",'//input[@id="LastName"]').send_keys("p")
driver.find_element("xpath",'//input[@id="Email"]').send_keys("abc123@gmail.com")
driver.find_element("xpath",'//input[@id="Password"]').send_keys("123dd45678")
driver.find_element("xpath",'//input[@id="ConfirmPassword"]').send_keys("123dd45678")
driver.find_element("xpath",'//input[@id="register-button"]').click()