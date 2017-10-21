import os
import sys
import pytest
import django

from pytest_bdd import parsers, scenarios, then, when
from splinter import Browser
from django.test.utils import setup_test_environment

sys.path.insert(0, "../")
from manage import DEFAULT_SETTINGS_MODULE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_SETTINGS_MODULE)
django.setup()
setup_test_environment()

scenarios('features')


@pytest.fixture
def django_browser():
    return Browser('django')


@when(parsers.parse('I browse to {url}'))
def go_to_url(url, django_browser):
    django_browser.visit(url)


@then('I see the login form')
def is_login_page(django_browser):
    django_browser.find_by_css('.form-signin').first
