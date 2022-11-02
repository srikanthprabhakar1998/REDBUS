import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
# driver.get("https://www.facebook.com/reg/")
# driver.maximize_window()
# driver.find_element("xpath",'//input[@name="firstname"]').send_keys("Srikanth")
# driver.find_element("xpath",'//input[@name="lastname"]').send_keys("p")
# driver.find_element("xpath",'//input[@name="reg_email__"]').send_keys("8904245128")
# driver.find_element("xpath",'//input[@data-type="password"]').send_keys("Srikky@123")
# dropdown = driver.find_element("xpath",'//select[@id="day"]')
# obj = Select(dropdown)
# time.sleep(1)
# obj.select_by_index(22)
# month = driver.find_element("xpath",'//select[@title="Month"]')
# obj1 = Select(month)
# obj1.select_by_index(11)
# yer = driver.find_element("xpath",'//select[@id="year"]')
# obj2 = Select(yer)
# obj2.select_by_value("1998")
# driver.find_element("xpath",'(//input[@name="sex"])[2]').click()
# driver.implicitly_wait(5)
# driver.find_element("xpath",'(//button[@type="submit"])[1]').click()



###############myntra######################

# driver.get("https://www.myntra.com/")

# driver.maximize_window()
# driver.find_element("xpath",'//input[@class="desktop-searchBar"]').send_keys("puma")
# driver.implicitly_wait(10)
# driver.find_element("xpath",'//li[.="Puma Shoes"]').click()

#Find the all object using visible and value both forword and revice direction
# driver.get(r'C:\Users\srika\PycharmProjects\Selenium1\html fiels\demo.html')
# cars = driver.find_element("xpath",'//select[@id="standard_cars"]')
# obj = Select(cars)
# all_options = obj.options
#####using indexing#############
# for index in range(len(all_options)):
#     obj.select_by_index(index)
#     time.sleep(1)


####using indexing and reversing#############
# for index in range(len(all_options)-1,-1,-1):
#     obj.select_by_index(index)
#     time.sleep(1)


#######using select by value###################
# for car in all_options:
#     obj.select_by_value(car.get_attribute("value"))


#######using select by value and reversing###################
# for car in (all_options)[::-1]:
#     obj.select_by_value(car.get_attribute("value"))




############using select by visible ################
# for car in all_options:
#     obj.select_by_visible_text(car.text)
#     time.sleep(1)


############using select by visible  and reversing################
# for car in all_options[::-1]:
#     obj.select_by_visible_text(car.text)
#     time.sleep(1)

######## All selected option##################
driver.get(r'C:\Users\srika\PycharmProjects\Selenium1\html fiels\demo.html')
cars = driver.find_element("xpath",'//select[@id="multiple_cars"]')
obj = Select(cars)
all_options = obj.options
obj.select_by_index(1)
obj.select_by_index(2)
p = obj.all_selected_options
for s in p :
    print(s.text)