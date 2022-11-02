from selenium import webdriver
# creat instance of chrome browser
c_path =r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
c_driver = webdriver.Chrome(executable_path=c_path)
print(c_driver)

# creat instance of firefox browser
f_path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\geckodriver.exe"
f_driver = webdriver.Firefox(executable_path=f_path)
print(f_driver)

# creat instance of edge browser
e_path=r"C:\Users\srika\PycharmProjects\Selenium1\driver\msedgedriver.exe"
e_driver = webdriver.Edge(executable_path=e_path)
print(e_driver)

