#path or url are store inthis file all
class Configuration:

    URL = "https://www.facebook.com/"
    # CHROME_PATH = r"C:\Users\Sanjana_Jadhav\PycharmProjects\Facebook sprint2\drivers\chromedriver.exe"
    CHROME_PATH = r"../drivers/chromedriver.exe"

    # FIREFOX_PATH = r"C:\Users\Sanjana_Jadhav\PycharmProjects\Facebook sprint2\drivers\geckodriver.exe"
    FIREFOX_PATH = r'../drivers/geckodriver.exe'

    # MSEDGE_PATH = r"C:\Users\Sanjana_Jadhav\PycharmProjects\Facebook sprint2\drivers\msedgedriver.exe"
    MSEDGE_PATH = r"../drivers/msedgedriver.exe"

    LOCATORS_PATH = r"C:\Users\Sanjana_Jadhav\PycharmProjects\Facebook sprint2\test_data\facebook_locator.xlsx"
    # LOCATORS_PATH = r'../test_data/facebook_locator.xlsx'

    TESTDATA_PATH = r"C:\Users\Sanjana_Jadhav\PycharmProjects\Facebook sprint2\test_data\facebook_test_data.xlsx"
    # TESTDATA_PATH = r'../test_data/facebook_test_data.xlsx'

    # REPORTS_PATH = r"C:\Users\Shree\PycharmProjects\HTD_Project\Reports\\"
    REPORTS_PATH = r"../Reports/"

    # SCREENSHOTS_PATH = r"C:\Users\Shree\PycharmProjects\HTD_Project\Screenshots\\"
    SCREENSHOTS_PATH = r"../Screenshots/"
    # gives report and screenshot folder path \\


    FRIENDS_LOCATOR_SHEET = "friend_locator"
    FRIENDS_TEST_DATASHEET = "frd_test_data"