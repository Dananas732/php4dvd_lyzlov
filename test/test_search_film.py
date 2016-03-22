# -*- coding: utf-8 -*-
from model.movie import Movie
import pytest
from fixture.application import Application
from model.user import User
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_search_real_movie(app):
    app.session.login(User.Admin())
    app.movie.search_film(Movie(film_name='name'))
    app.movie.wait_load_page('name')
    #film = app.movie.get_movie_list()
    #assert len(film) > 0
    app.session.logout()



def test_search_not_real_movie(app):
    app.session.login(User.Admin())
    app.movie.search_film(Movie(film_name='ZZZZZZZZZZ'))
    #assert app.wd.current_url == app.base_url + "/php4dvd/#!/search/ZZZZZZZZZZ/sort/name asc/"
    app.movie.wait_empty_page()
    #film = app.movie.get_movie_list()
    #assert len(film) > 0
    app.session.logout()