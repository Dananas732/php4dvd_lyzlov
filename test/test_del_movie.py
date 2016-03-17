__author__ = 'e.lyzlov'
import pytest
from fixture.application import Application
import random

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_del_movie(app):
    app.session.login(username='admin', password='admin')
    select_film = app.movie.get_movie_list()
    film = random.choice(select_film)
    app.movie.del_film_by_id(film)
    app.session.logout()
