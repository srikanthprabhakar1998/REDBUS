from selenium import webdriver
path=r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get(r'//www.flipkart.com/')
driver.find_element("xpath", '//input[@name="q"]').send_keys("nike shoes")
