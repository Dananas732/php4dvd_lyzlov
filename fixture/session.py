__author__ = 'e.lyzlov'

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys(user.username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(user.password)
        wd.find_element_by_name("submit").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Log out").click()
        wd.switch_to_alert().accept()