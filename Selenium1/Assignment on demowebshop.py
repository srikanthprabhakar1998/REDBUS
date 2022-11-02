import time
# from selenium import webdriver
# path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
# driver =webdriver.Chrome(executable_path=path)
# driver.get(r"https://demowebshop.tricentis.com/")
# driver.find_element("xpath",'(//a[@href="/books"])[3]').click()
# driver.find_element("xpath",'(//input[@value="Add to cart"])[1]').click()
# time.sleep(2)
# driver.find_element("xpath",'(//input[@value="Add to cart"])[2]').click()
# time.sleep(2)
# driver.find_element("xpath",'(//input[@value="Add to cart"])[3]').click()


'''1.Write xpath of “add to cart” button of “health”, “fiction”, ”computing and internet” books in demowebshop'''
# from selenium import webdriver
# path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
# driver =webdriver.Chrome(executable_path=path)
# driver.get(r"https://demowebshop.tricentis.com/")
# driver.maximize_window()
# book_name = ["Computing and Internet","Fiction","Health Book"]
# for book in book_name:
#     driver.find_element("xpath",
#     f'//div[@class = "details"]//h2[@class = "product-title"]//a[text()="{book}"]/../..//div[@class = "buttons"]//input[@class = "button-2 product-box-add-to-cart-button"]').click()
#     time.sleep(2)



'''2.Write xpath of radio button corresponding to rating “good”, “excellent”, “poor”, “very bad” in demowebshop'''
# driver.get("https://demowebshop.tricentis.com")
# driver.maximize_window()

# community_poll = ["Good","Poor","Very bad","Excellent"]
# for poll in community_poll:
#     if poll == "Excellent":
#         driver.find_element("xpath",
#         '//li[@class = "answer"]//input[@id = "pollanswers-1"]/..//label[text()="Excellent"]').click()
#         time.sleep(2)
#     elif poll == "Good":
#         driver.find_element("xpath",
#         '//li[@class = "answer"]//input[@id = "pollanswers-2"]/..//label[text()="Good"]').click()
#         time.sleep(2)
#     elif poll == "Poor":
#         driver.find_element("xpath",
#         '//li[@class = "answer"]//input[@id = "pollanswers-3"]/..//label[text()="Poor"]').click()
#         time.sleep(2)
#     elif poll == "Very bad":
#         driver.find_element("xpath",
#         '//li[@class = "answer"]//input[@id = "pollanswers-4"]/..//label[text()="Very bad"]').click()
#         time.sleep(2)

##########################################################################
'''5. Get link text of all footer links in smart bear webpage'''
# driver.get("https://smartbear.com/")

# list_footer_name = ["AlertSite","BitBar","Bugsnag","Capture for Jira","Collaborator","Cucumber for Jira","CucumberStudio","Cucumber Open","LoadNinja","Pact","Pactflow","ReadyAPI","SoapUI","Swagger","SwaggerHub","TestComplete","TestEngine","TestLeft","Zephyr"]
# for footer in list_footer_name:
#     element = driver.find_element("xpath", f'//ul[@class = "mb-0"]//li//a[text() = "{footer}"]')
#     print(element.text)

##############################################################################3
'''8. Check all the checkbox’s in reversed order in demo.html'''
# file_path = r'C:\Users\Shree\PycharmProjects\Selenium\HTML files\demo.html'
# driver.get(file_path)
#
# languages = ["Ruby","Java","Perl","Python","C#","JavaScript"]
# res = languages[::-1]
#
# for language in res:
#
#     driver.find_element("xpath", f'//td[text() = "{language}"]/..//input[@name = "download"]').click()
#     time.sleep(2)


###############################################################################
'''9.Check alternate checkbox’s in demo.html'''
# file_path = r'C:\Users\Shree\PycharmProjects\Selenium\HTML files\demo.html'
# driver.get(file_path)
#
# languages = ["Ruby","Java","Perl","Python","C#","JavaScript"]
# res = languages[::2]
# for language in res:
#
#     driver.find_element("xpath", f'//td[text() = "{language}"]/..//input[@name = "download"]').click()
#     time.sleep(2)

###############################################################################
'''10. Check first and last checkbox in demo.html'''
# file_path = r'C:\Users\Shree\PycharmProjects\Selenium\HTML files\demo.html'
# driver.get(file_path)
#
# languages = ["Ruby","Java","Perl","Python","C#","JavaScript"]
# driver.find_element("xpath", f'//td[text() = "{languages[0]}"]/..//input[@name = "download"]').click()
# time.sleep(2)
# driver.find_element("xpath", f'//td[text() = "{languages[-1]}"]/..//input[@name = "download"]').click()
# time.sleep(2)




####################question5################

# driver.get(r"https://smartbear.com/")
# time.sleep(1)
# lists = driver.find_elements("xpath",'//div[@class="product-column col-12"]//a')
# print(len(lists))
# for list in lists:
#     print(list.text)
# driver.close()

#####################question8#######################
# file_path = r'C:\Users\srika\PycharmProjects\Selenium1\html fiels\demo.html'
# driver.get(file_path)
# languages = ["JavaScript","Perl","Ruby","Java","Python","C#"]
# res = languages[::-1]
# for language in res:
#     driver.find_element("xpath", f'//td[.="{language}"]/..//input[@type="checkbox"]').click()
#     time.sleep(1)

#################question9##########################

# file_path = r'C:\Users\srika\PycharmProjects\Selenium1\html fiels\demo.html'
# driver.get(file_path)
# languages = ["JavaScript","Perl","Ruby","Java","Python","C#"]
# res = languages[::2]
# for language in res:
#     driver.find_element("xpath", f'//td[.="{language}"]/..//input[@type="checkbox"]').click()
#     time.sleep(1)

#####################question10#####################
# file_path = r'C:\Users\srika\PycharmProjects\Selenium1\html fiels\demo.html'
# driver.get(file_path)
# languages = ["JavaScript","Perl","Ruby","Java","Python","C#"]
# driver.find_element("xpath", f'//td[.="{languages[0]}"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath", f'//td[.="{languages[-1]}"]/..//input[@type="checkbox"]').click()
# time.sleep(1)


