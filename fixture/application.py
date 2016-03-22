__author__ = 'e.lyzlov'
from fixture.session import SessionHelper
from fixture.movie import MovieHelper

class Application(object):

    def __init__(self, WebDriver):
        self.wd = WebDriver()
        self.base_url = "http://localhost/"
        self.session = SessionHelper(self)
        self.movie = MovieHelper(self)


    def open_add_movie_page(self):
        wd = self.wd
        wd.get(self.base_url + "/php4dvd/?go=add")

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url + "/php4dvd/")

    def destroy(self):
        self.wd.quit()