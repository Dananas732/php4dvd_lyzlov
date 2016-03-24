__author__ = 'e.lyzlov'
from fixture.session import SessionHelper
from fixture.movie import MovieHelper
#from fixture.waiter import WaitHelper
from selenium.webdriver.support.wait import WebDriverWait


class Application(object):

    def __init__(self, driver):
        self.wd = driver
        self.base_url = "http://localhost/"
        self.session = SessionHelper(self)
        self.movie = MovieHelper(self)
    #    self.wait = WaitHelper(self)
        self.wait = WebDriverWait(self.wd, 30)

    def wait(self, element):
        self.wait.until(staleness_of(element))

    def open_add_movie_page(self):
        wd = self.wd
        wd.get(self.base_url + "/php4dvd/?go=add")

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url + "/php4dvd/")

    def destroy(self):
        self.wd.quit()