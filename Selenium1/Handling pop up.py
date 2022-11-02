import time

from selenium import webdriver
path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
# driver.get(r"C:\Users\srika\PycharmProjects\Selenium1\html fiels\demo.html")
# ele = driver.find_element("xpath",'//button[@id="double-click"]')

#########################simple alert########################
# driver.find_element("id","submit").click()
# time.sleep(2)
# alert_obj = driver.switch_to.alert
# alert_obj.accept()

#####################conformation alert#######################
# driver.find_element("id","delete").click()
# time.sleep(1)
# alert_obj = driver.switch_to.alert
# alert_obj.dismiss()


#########################iframes##################################
# driver.get(r"C:\Users\srika\PycharmProjects\Selenium1\html fiels\iframe.html")
# driver.switch_to.frame("FR1")
# driver.find_element("xpath",'//input[@id="small-searchterms"]').send_keys("mobiles")
# driver.switch_to.frame("FR2")

######################child browser########################################
# driver.get("https://demowebshop.tricentis.com/")
# driver.find_element("xpath",'//a[. = "Facebook"]').click()
# driver.implicitly_wait(10)
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
# driver.find_element("xpath",'//Input[@name ="email"]').send_keys("8904245127")

########################file upload pop up ###################################
driver.get("https://www.monsterindia.com/")
driver.find_element("xpath",'//span[.="Upload Resume"]').click()
path1 = r"C:\Users\srika\PycharmProjects\Selenium1\html fiels\sri.txt"
driver.find_element("xpath",'(//input[@type="file"])[1]').send_keys(path1)
