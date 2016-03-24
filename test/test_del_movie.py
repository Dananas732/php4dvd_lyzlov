__author__ = 'e.lyzlov'
from model.user import User
from fixture.selenium_fixture import app
import random



def test_del_movie(app):
    app.session.login(User.Admin())
    select_film = app.movie.get_movie_list()
    film = random.choice(select_film)
    app.movie.del_film_by_id(film)
    app.session.logout()
