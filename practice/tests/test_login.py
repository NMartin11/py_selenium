import pytest

""""

Next steps:
    * have selenium fixture passed to HerokuappPage
        * will allow to have every new page use the same methods
            which now are using WebDriverWaits
    * change test_login_succeeded to use herokuappPage instead of straight selenium
"""
def test_login_succeeded(driver, selenium):
    selenium.go_to_herokuapp()
    selenium.type_by_id('username', 'tomsmith')
    selenium.type_by_id('password','SuperSecretPassword!')
    selenium.click_by_css("button[type='submit']")
    assert driver.find_element_by_css_selector("div.flash.success").is_displayed()

if __name__ == "__main__":
    pytest.main()

