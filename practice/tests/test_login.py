import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestHerokuapp(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome('/home/nathan/py3env/chromedriver/chromedriver')

    def test_login_succeeded(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/login")

        driver.find_element_by_id('username').send_keys('tomsmith')
        driver.find_element_by_id('password').send_keys('SuperSecretPassword!')

        submit_button = driver.find_element_by_css_selector("button[type='submit']")
        submit_button.click()

        self.assertTrue(driver.find_element_by_css_selector("div.flash.success").is_displayed())

    @classmethod
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

