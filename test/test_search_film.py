# -*- coding: utf-8 -*-
from model.movie import Movie
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_search_real_movie(app):
    app.session.login(username='admin', password='admin')
    app.movie.search_film(Movie(film_name='name'))
    film = app.movie.get_movie_list()
    assert len(film) > 0
    app.session.logout()


def test_search_not_real_movie(app):
    app.session.login(username='admin', password='admin')
    app.movie.search_film(Movie(film_name='ZZZZZZZZZZ'))
    film = app.movie.get_movie_list()
    assert len(film) > 0
    app.session.logout()