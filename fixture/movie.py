__author__ = 'e.lyzlov'

class MovieHelper:

    def __init__(self, app):
        self.app = app


    def add_movie(self, film):
        wd = self.app.wd
        self.app.open_add_movie_page()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(film.film_name)
        wd.find_element_by_name("year").clear()
        wd.find_element_by_name("year").send_keys(film.film_year)
        wd.find_element_by_id("submit").click()
        self.app.open_home_page()

    def check_field(self):
        wd = self.app.wd
        self.app.open_add_movie_page()
        wd.find_elements_by_xpath("//div[@class='addmovie']//input[@name='name'][@class='required error']")
        wd.find_elements_by_xpath("//div[@class='addmovie']//input[@name='name'][@class='required digits error']")
        wd.getCurrentUrl().AssertEquals(self.app.base_url + "/php4dvd/?go=add")

