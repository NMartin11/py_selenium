from selenium.webdriver.common.by import By


class HerokuappPage(object):
    username_field = By.ID('username')
    password_field = By.ID('password')
    submit_button = By.CSS_SELECTOR("button[type='submit']")
    success_banner = By.CSS_SELECTOR('div.flash.success')

