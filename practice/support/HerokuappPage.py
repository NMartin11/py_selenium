from page_objects import PageObject, PageElement
from practice.conftest import pages


class HerokuappPage(PageObject, PageElement):
    username_field = PageElement(id_='username')
    password_field = PageElement(id_='password')
    submit_button = PageElement(css="button[type='submit']")



    def fill_username_field(self, username):
        self.username_field = username

    def fill_password_field(self, password):
        self.password_field = password

    def submit_login_form(self):
        self.submit_button.click()


