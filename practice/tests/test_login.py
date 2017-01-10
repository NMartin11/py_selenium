import pytest
from practice.support import HerokuappPage




def test_login_succeeded(driver):
    driver.get("http://the-internet.herokuapp.com/login")
    page = HerokuappPage.HerokuappPage(driver)
    page.fill_username_field('tomsmith')
    page.fill_password_field('SuperSecretPassword!')
    page.submit_login_form()

    assert driver.find_element_by_css_selector("div.flash.success").is_displayed()


if __name__ == "__main__":
    pytest.main()

