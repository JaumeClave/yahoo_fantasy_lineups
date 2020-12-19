# Import modules
import time
from selenium import webdriver
from selenium.webdriver import Chrome


# Declare variables
CHROME_USER_DATA_DIRECTORY_ARGUMENT = r"user-data-dir=C:\Users\Jaume\AppData\Local\Google\Chrome" \
                                      r"\User Data\Python"
CHROME_DISABLE_NOTIFICATION_ARGUMENT = "--disable-notifications"
CHROME_EXECUTABLE_PATH = r"C:\Users\Jaume\Documents\Python " \
                         r"Projects\yahoo_fantasy_lineups\chromedriver.exe"

MY_TEAM_URL = "https://basketball.fantasysports.yahoo.com/nba/55374/6"

SLEEP_SECONDS = 1

START_ACTIVE_PLAYERS_BUTTON_XPATH_TEXT = "//*[(text()='Start Active Players')]"
REST_OF_WEEK_START_BUTTON_XPATH_TEXT = "//*[(text()='Start')]"


# Functions
def open_yahoo_my_team():
    """

    :return:
    """
    # Load Profile
    options = webdriver.ChromeOptions()

    # Load Chrome profile and download directory
    options.add_argument(CHROME_USER_DATA_DIRECTORY_ARGUMENT)
    options.add_argument(CHROME_DISABLE_NOTIFICATION_ARGUMENT)

    # Chrome with profile
    driver = Chrome(CHROME_EXECUTABLE_PATH, chrome_options=options)

    driver.get(MY_TEAM_URL)
    time.sleep(SLEEP_SECONDS)

    return driver


def click_button_yahoo_my_team(driver, button_xpath_text):
    """

    :param button_xpath_text:
    :return:
    """
    webelement_button = driver.find_element_by_xpath(button_xpath_text)
    webelement_button.click()
    time.sleep(SLEEP_SECONDS)

    return driver


def set_daily_yahoo_lineups():
    driver = open_yahoo_my_team()
    click_button_yahoo_my_team(driver, START_ACTIVE_PLAYERS_BUTTON_XPATH_TEXT)
    click_button_yahoo_my_team(driver, REST_OF_WEEK_START_BUTTON_XPATH_TEXT)
    driver.close()

    return None


if __name__ == "__main__":
    set_daily_yahoo_lineups()

