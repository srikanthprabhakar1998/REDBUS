from selenium import webdriver
path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path= path)
driver.get(r"C:\Users\srika\PycharmProjects\Selenium1\html fiels\css_selector.html")
driver.maximize_window()
driver.find_element("css selector", 'input[type="text"]').send_keys("user1")
driver.find_element("css selector", 'input[type="password"]').send_keys("pwd")