import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects import PageElement, PageObject


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="chrome", help="Type in browser type")
    parser.addoption("--url", action="store", default="http://www.google.com", help="url")
    parser.addoption("--username", action="store", default="manager", help="username")
    parser.addoption("--password", action="store", default="test", help="password")


@pytest.fixture(scope="module", autouse=True)
def driver(request):
    browser = request.config.getoption("--driver")
    if browser == 'chrome':
        browser = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
        browser.get("default:blank")
        browser.implicitly_wait(10)
        request.addfinalizer(browser.quit)
        return browser
    else:
        print('Only Works with chrome')


@pytest.fixture
def selenium(driver):
    class Selenium():
        def __init__(self):
            self.driver = driver

        def url(self, name):
            driver.get(name)

        def go_to_herokuapp(self):
            driver.get("http://the-internet.herokuapp.com/login")

        def click_by_css(self, css):
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
            element.click()

        def click_by_id(self, id):
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, id)))
            element.click()

        def click_by_xpath(self, xpath):
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element.click()

        def type_by_id(self, id, text):
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, id)))
            element.send_keys(text)

    return Selenium()
