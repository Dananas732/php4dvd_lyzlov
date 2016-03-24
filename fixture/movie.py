__author__ = 'e.lyzlov'
from selenium.webdriver.common.keys import Keys



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

    def check_field_in_add_form(self):
        wd = self.app.wd
        self.app.open_add_movie_page()
        wd.find_element_by_xpath("//div[@class='addmovie']//input[@name='name'][@class='required error']")
        wd.find_element_by_xpath("//div[@class='addmovie']//input[@name='year'][@class='required digits error']")
        wd.find_element_by_xpath("//div[@class='button']//img[@title='Save'][@alt='Save']").click()
        assert wd.current_url == self.app.base_url + "/php4dvd/?go=add"
        self.app.open_home_page()

    films_list = None

    def get_movie_list(self):
        if self.films_list is None:
            wd = self.app.wd
            self.films_list = []
            for element in wd.find_elements_by_xpath("//div[@class='movie_box']"):
                id = element.get_attribute("id")
                self.films_list.append(id)
        return list(self.films_list)


    def select_film_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='%s']" % id).click()

    def del_film_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_film_by_id(id)
        wd.find_element_by_xpath("//img[@title='Remove'][@alt='Remove']").click()
        wd.switch_to_alert().accept()

    def search_film(self, film):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//div[@class='searchbox']/input[@id='q']").clear()
        wd.find_element_by_xpath("//div[@class='searchbox']/input[@id='q']").send_keys(film.film_name)
        wd.find_element_by_xpath("//div[@class='searchbox']/input[@id='q']").send_keys(Keys.RETURN)

    def check_film_list(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='results']/div[@class='content']").send_keys(Keys.ENTER)