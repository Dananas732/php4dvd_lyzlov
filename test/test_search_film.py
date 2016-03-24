# -*- coding: utf-8 -*-
from model.movie import Movie
from model.user import User
from fixture.selenium_fixture import app


def test_search_real_movie(app):
    app.session.login(User.Admin())
    element = app.wd.find_elements_by_xpath("//div[@class='movie_box']")
    app.movie.search_film(Movie(film_name='name'))
    app.wait(element)
  #  wait_load_page('name')
    app.session.logout()



def test_search_not_real_movie(app):
    app.session.login(User.Admin())
    app.movie.search_film(Movie(film_name='ZZZZZZZZZZ'))
    app.movie.wait_empty_page()
    app.session.logout()