__author__ = 'e.lyzlov'
'''
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class WaitHelper:

    def __init__(self, app, driver):
        wd = self.app.wd
        self.app = app
        self.wait = WebDriverWait(wd, 30)

    def wait(self):
        self.wait.until(self.wait.staleness_of(By.XPATH,"//div[@class='movie_box']"))


    element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav, #loginform")))
        if element.tag_name == "nav":
            # we are on internal page
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()
        self.login(user)


    def wait_empty_page(self):
        for i in range(60):
            try:
                if len(app.movie.get_movie_list()) == 0: break
            except: pass

    def wait_load_page(self, par):
        wd = self.app.wd
        for i in range(60):
            try:
                if wd.current_url == self.app.base_url + "/php4dvd/#!/search/'%s'/sort/name%20asc/" % par: break
            except: pass

'''