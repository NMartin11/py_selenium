import pytest
from practice.support import HerokuappPage




def test_login_succeeded(driver, pages):
    # driver.get("http://the-internet.herokuapp.com/login")
    pages.url("http://the-internet.herokuapp.com/login")
    heroPage = HerokuappPage.HerokuappPage(driver)
    heroPage.fill_username_field('tomsmith')
    heroPage.fill_password_field('SuperSecretPassword!')
    # heroPage.submit_login_form()
    pages.click_by_css("button[type='submit']")

    assert driver.find_element_by_css_selector("div.flash.success").is_displayed()


if __name__ == "__main__":
    pytest.main()

