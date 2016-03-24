__author__ = 'e.lyzlov'
# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from fixture.application import Application

@pytest.fixture
def app(request):
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    request.addfinalizer(driver.quit)
    return Application(driver)