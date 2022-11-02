import time

from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given(u'open the browser and enter the url')
def open_browser(context):
    path = r"C:\Users\srika\PycharmProjects\BDD_RedBus\drivers\chromedriver.exe"
    context.driver = webdriver.Chrome(executable_path=path)
    context.driver.get("https://www.redbus.in/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)


@when(u'user is able to click on the manage bookings')
def click_Manager_Booking(context):
    context.driver.find_element("xpath", '//div[@class="manageHeaderLbl"]').click()


@then(u'user is able to click on the show my tickets')
def select_Show_my_ticket(context):
    context.driver.find_element("xpath", '//span[contains(text(),"Show My Ticket")]').click()


@then(u'user is able to enter data into the TICKET NUMBER textfield "{f_name}"')
def enter_From_textfield(context, f_name):
    # if isinstance(f_name, float):
    #     f_name = str(f_name)
    context.driver.find_element("xpath", '//input[@id="searchTicketTIN"]').send_keys(f_name)


@then(u'user is bale to enter data into the MOBILE NUMBER textfield "{l_name}"')
def enter_To_textfield(context, l_name):
    context.driver.find_element("xpath", '//input[@name="mobileno"]').send_keys(l_name)
    time.sleep(5)


@then(u'user is able to click on submit')
def click_Submit_button(context):
    context.driver.find_element("xpath", '//input[@id="ticketSearch"]').click()
    time.sleep(2)
    wait_ = WebDriverWait(context.driver, 15)
    assert wait_.until(expected_conditions.title_contains("redBus revamp"))



@then(u'close browser')
def close_browser(context):
    context.driver.quit()
