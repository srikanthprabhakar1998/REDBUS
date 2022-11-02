from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
# driver.get("https://www.myntra.com")
# ele = driver.find_element("xpath",'//a[@data-group="men"]')
# obj = ActionChains(driver)
# obj.move_to_element(ele).perform()



#######################double click###################################
# driver.get(r"C:\Users\srika\PycharmProjects\Selenium1\html fiels\demo.html")
# ele = driver.find_element("xpath",'//button[@id="double-click"]')
# obj = ActionChains(driver)
# obj.double_click(ele)

##############################select all ###############################
# driver.get(r"C:\Users\srika\PycharmProjects\Selenium1\html fiels\demo.html")
# ele = driver.find_element("xpath",'//button[@id="double-click"]')
# obj = ActionChains(driver)
# obj.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()


