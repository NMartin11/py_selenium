import pytest
from selenium import webdriver
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
def pages(driver):
    class Pages(object):
        def url(self, name):
            driver.get(name)

        def click_by_element(self, element):
            e = PageElement(element)
            e.click()

        def click_by_id(self, id):
            element =  PageElement(id_='id')
            element.click

        def click_by_css(self, css):
            element = PageElement(css=css)
            element.click()

    return Pages()















