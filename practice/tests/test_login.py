import unittest
from selenium import webdriver
from practice.support import  page
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase, page.MainPage, page.SearchResultsPage):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.is_title_matches()
        elem = driver.find_element_by_name('q')
        elem.send_keys("pycon")
        self.click_go_button()
        assert self.is_results_found()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()