from selenium import webdriver
path =r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
driver= webdriver.Chrome(executable_path=path)
driver.get(r'https://demo.actitime.com/login.do')
driver.find_element("css selector",'input[id="username"]').send_keys("admin")
driver.find_element("css selector",'input[placeholder="Password"]').send_keys("manager")
driver.find_element("css selector",'a[id="loginButton"]>div').click()