import pytest
from selenium import webdriver
from library.config import Configuration
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture(params=["Chrome"])
def init_driver(request):
    browser = request.param 

    if browser.lower() == "chrome":
        chrome_path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=Configuration.CHROME_PATH)
    elif browser.lower() == "firefox":
        firefow_path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\geckodriver.exe"
        driver = webdriver.Firefox(executable_path=Configuration.FIREFOX_PATH)
    else:
        edge_path = r"C:\Users\srika\PycharmProjects\Selenium1\driver\msedgedriver.exe"
        driver = webdriver.Edge(executable_path=Configuration.MSEDGE_PATH)

    driver.get(Configuration.URL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
