import os
import sys
import pytest
import django

from pytest_bdd import parsers, scenarios, given, when, then
from splinter import Browser
from django.test.utils import setup_test_environment
from django.contrib import auth

sys.path.insert(0, "../")
from manage import DEFAULT_SETTINGS_MODULE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_SETTINGS_MODULE)
django.setup()
setup_test_environment()

from django.contrib.auth.models import User

scenarios('features')


@pytest.fixture
def django_browser():
    return Browser('django')


@given(parsers.parse('a user \'{username}\' exists with password \'{password}\''))
def create_user(username, password):
    try:
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
    except User.DoesNotExist:
        User.objects.create_user(username, password=password)


@when(parsers.parse('I browse to {url}'))
def go_to_url(url, django_browser):
    django_browser.visit(url)


@when(parsers.parse('login with username \'{username}\' and password \'{password}\''))
def login(username, password, django_browser):
    django_browser.find_by_id('id_username').first.fill(username)
    django_browser.find_by_id('id_password').first.fill(password)
    django_browser.find_by_css('.btn').first.click()


@then('I see the login form')
def is_login_page(django_browser):
    django_browser.find_by_css('.form-signin').first


# Currently tests if login redirects to home page as I'm not sure how to test if user is authenticated using splinter
@then('I am successfully logged in and directed to the home page')
def is_logged_in(django_browser):
    assert django_browser.url == '/'