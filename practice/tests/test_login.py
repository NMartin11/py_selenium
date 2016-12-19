import pytest
from selenium import webdriver


def test_login_succeeded():
    driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
    driver.get("http://the-internet.herokuapp.com/login")

    driver.find_element_by_id('username').send_keys('tomsmith')
    driver.find_element_by_id('password').send_keys('SuperSecretPassword!')

    submit_button = driver.find_element_by_css_selector("button[type='submit']")
    submit_button.click()

    assert driver.find_element_by_css_selector("div.flash.success").is_displayed()
    driver.close()

if __name__ == "__main__":
    pytest.main()

