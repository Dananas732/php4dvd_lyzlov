# -*- coding: utf-8 -*-
from model.movie import Movie
from model.user import User
from fixture.selenium_fixture import app


def test_add_movie(app):
    app.session.login(User.Admin())
    old_list = app.movie.get_movie_list()
    app.movie.add_movie(Movie(film_name='name', film_year='2016'))
    new_list = app.movie.get_movie_list()
    assert old_list == new_list
    app.session.logout()


def test_add_movie_empty(app):
    app.session.login(User.Admin())
    app.movie.check_field_in_add_form()
    app.session.logout()
