import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# action_obj = ActionChains(driver)


@given(u'Open the browser and enter the valid url')
def launch_browser(context):
    # context.c_path = r'C:\Users\srika\PycharmProjects\Facebook sprint2\drivers\chromedriver.exe'
    # context.driver = webdriver.Chrome(executable_path=context.c_path)
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.facebook.com/")
    context.driver.maximize_window()
    time.sleep(1)


@when(u'Enter the Username"{username_}"')
def enter_user_name(context, username_):
    time.sleep(3)
    context.driver.find_element("xpath", '//input[@id="email"]').send_keys(username_)
    time.sleep(2)


@when(u'Enter the Password"{pwd}"')
def enter_password_btn(context, pwd):
    context.driver.find_element("xpath", '//input[@id="pass"]').send_keys(pwd)
    time.sleep(3)


@when(u'Click on login button')
def login_btn(context):
    context.driver.find_element("xpath", '//button[@name="login"]').click()
    time.sleep(3)


@when(u'Click on friends button')
def frd_btn(context):
    context.driver.find_element("xpath", '//a[@aria-label="Friends"]').click()


@when(u'Click on new message button')
def new_msg(context):
    context.driver.find_element("xpath", '//div[@class="x191j7n5 x92rtbv x10l6tqk x1useyqa"]').click()
    # context.driver.find_element("xpath", '//div[@aria-label="New Message"]').click()


@when(u'Click on friend request button')
def frd_req_btn(context):
    context.driver.find_element("xpath",'(//div[@aria-label="Friends"]//span[text()="Friend requests"])[1]').click()
    # context.driver.find_element("xpath", '(//div[@aria-label="Friends"])[1]//span[text()="Friend requests"]').click()


@when(u'Click on confirm request')
def confirm_req(context):
    context.driver.find_element("xpath", '(//div[@aria-label="Confirm"])[3]').click()


@when(u'Click on sent request link')
def sent_request_link(context):
    context.driver.find_element("xpath", '//span[text()="View sent requests"]').click()


@when(u'Click on delete request')
def delete_req(context):
    context.driver.find_element("xpath", '(//div[@class="x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou x1qhmfi1 x1r1pt67"])[2]').click()


@when(u'Click on suggestion button')
def suggestion_btn(context):
    context.driver.find_element("xpath", '//span[text()="Suggestions"]').click()


@when(u'Click on add friend button')
def add_frd_btn(context):
    context.driver.find_element("xpath",'(//span[text()="Add Friend"])[1]')click()


@when(u'Click on remove friend button')
def remove_frd_btn(context):
    .click()


@when(u'Click on all friend button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on all friend button').click()


@when(u'Click on search bar')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on search bar')


@when(u'Click on search dot')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on search dot')


@when(u'Click on message button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on message button')


@when(u'Click on block button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on block button')


@when(u'Click on unfriend button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on unfriend button')


@when(u'Click on Birthday button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on Birthday button')


@when(u'Click on name link')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on name link')


@when(u'Click on custom list')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on custom list')


@when(u'Click on close friend button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on close friend button')


@when(u'Click on fav button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on fav button')


@when(u'Click on frds button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on frds button')


@when(u'Click on notification settings button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on notification settings button')


@when(u'Click on notification dot button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on notification dot button')

@then('Close the browser')
def close_browser(context):
    context.driver.close()



