import time
from selenium import webdriver
path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
driver=webdriver.Chrome(executable_path=path)
url = "https://www.youtube.com/"
driver.get(url)
# driver.maximize_window()
# time.sleep(2)
# driver.minimize_window()
# time.sleep(2)
# driver.fullscreen_window()
# print(driver.get_window_position())
# print(driver.get_window_size())
# print(driver.get_window_rect())

#refresh, back, forward
# driver.refresh()
# driver.back()
# time.sleep(2)
# driver.forward()

#close , quit
# driver.close()
driver.quit()

#nam
print(driver.title)
print(driver.name)
print(driver.current_url)