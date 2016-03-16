# -*- coding: utf-8 -*-
from model.movie import Movie
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_movie(app):
    app.session.login(username='admin', password='admin')
    app.movie.add_movie(Movie(film_name='name', film_year='2016'))
    app.session.logout()


def test_add_movie_empty(app):
    app.session.login(username='admin', password='admin')
    app.movie.check_field()
    app.session.logout()
