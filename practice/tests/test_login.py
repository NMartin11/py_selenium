import pytest
from practice.support import HerokuappPage
from selenium import webdriver


def test_login_succeeded(driver):
    driver.get("http://the-internet.herokuapp.com/login")
    page = HerokuappPage(driver)
    page.username_field = 'tomsmith'
    page.password_field = 'SuperSecretPassword!'
    page.submit_button.click()

    # driver.find_element_by_id('username').send_keys('tomsmith')
    # driver.find_element_by_id('password').send_keys('SuperSecretPassword!')
    #
    # submit_button = driver.find_element_by_css_selector("button[type='submit']")
    # submit_button.click()
    assert driver.find_element_by_css_selector("div.flash.success").is_displayed()

if __name__ == "__main__":
    pytest.main()

