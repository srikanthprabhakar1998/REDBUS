from selenium import webdriver
path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)



#######question1########################3

# driver.get(r"C:\Users\srika\PycharmProjects\Selenium1\html fiels\css_selector.html")
# driver.find_element("xpath", "(//input[@class='first_row'])[1]").send_keys("hello")
# driver.find_element("xpath", "(//input[@class='first_row'])[2]").send_keys("world")
# driver.find_element("xpath", "(//input[@class='first_row'])[3]").send_keys("welcome")
# driver.find_element("xpath", "(//input[@class='second_row'])[1]").send_keys("to")
# driver.find_element("xpath", "(//input[@class='second_row'])[2]").send_keys("python")
# driver.find_element("xpath", "(//input[@class='second_row'])[3]").send_keys("hi")
# driver.find_element("xpath", "(//input[@class='third_row'])[1]").send_keys("selenium")
# driver.find_element("xpath", "(//input[@class='third_row'])[2]").send_keys("browser")
# driver.find_element("xpath", "(//input[@class='third_row'])[3]").send_keys("automation")

##########question2#####################
# driver.get("https://www.python.org/")
# driver.maximize_window()
# element=driver.find_elements("tag name", "a")
# for item in element:
#     print(item.text)
# driver.close()

# ################question3#################
# driver.get("https://www.python.org/")
# driver.maximize_window()
# element = driver.find_elements("xpath", '//a[contains(.,"Python")]')
# for item in element:
#     print(item.text)
# # driver.close()

################question5#################
# driver.get("https://services.smartbear.com/samples/testcomplete14/smartstore")
# driver.maximize_window()
# element= driver.find_elements("xpath", '//img')
# for i in element:
#     print(i.get_attribute("alt"))
# driver.close()


###############question4###################
