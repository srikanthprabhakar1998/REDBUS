import time

from selenium import webdriver
path =r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
driver =webdriver.Chrome(executable_path=path)
driver.get(r'C:\Users\srika\PycharmProjects\Selenium1\html fiels\demo.html')
driver.maximize_window()
# driver.find_element("xpath",'//td[.="Perl"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath",'//td[.="Ruby"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath",'//td[.="Java"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath",'//td[.="Python"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath",'//td[.="C#"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath",'//td[.="JavaScript"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath",'//td[.="Perl"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath",'//td[.="Ruby"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath",'//td[.="Java"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath",'//td[.="Python"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath",'//td[.="C#"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath",'//td[.="JavaScript"]/..//input[@type="checkbox"]').click()

languages = ["JavaScript","Perl","Ruby","Java","Python","C#"]
for language in languages:
    driver.find_element("xpath", f'//td[.="{language}"]/..//input[@type="checkbox"]').click()


