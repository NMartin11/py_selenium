from page_objects import PageObject, PageElement


class HerokuappPage(PageObject):
    username_field = PageElement(id_='username')
    password_field = PageElement(id_='password')
    submit_button = PageElement(css="button[type='submit'")