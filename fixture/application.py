__author__ = 'e.lyzlov'
from fixture.session import SessionHelper
from fixture.movie import MovieHelper
#from fixture.waiter import WaitHelper
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *

class Application(object):

    def __init__(self, driver):
        self.wd = driver
        self.base_url = "http://localhost/"
        self.session = SessionHelper(self)
        self.movie = MovieHelper(self)
    #    self.wait = WaitHelper(self)
        self.wait = WebDriverWait(self.wd, 30)

    def wait_element_off(self, element):
        self.wait.until(staleness_of(element))

    def wait_element_on(self):
        wd = self.wd
        element = self.wait.until(presence_of_element_located((By.XPATH, "//div[@class='movie_box']")))
        if element != wd.find_element_by_xpath("//div[@class='movie_box']"):
            pass
        #self.session.logout()

    def open_add_movie_page(self):
        wd = self.wd
        wd.get(self.base_url + "/php4dvd/?go=add")

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url + "/php4dvd/")

    def destroy(self):
        self.wd.quit()