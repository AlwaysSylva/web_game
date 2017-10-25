from behave import given, when, then
from test.factories.user import UserFactory


@given('a user \'{username}\' exists with password \'{password}\'')
def create_user(context, username, password):
    from django.contrib.auth.models import User
    user = UserFactory(username=username)
    user.set_password(password)
    user.save()


@when('I browse to {url}')
def go_to_url(context, url):
    context.browser.visit(context.get_url(url))


@when('login with username \'{username}\' and password \'{password}\'')
def login(context, username, password):
    context.browser.fill("username", username)
    context.browser.fill("password", password)
    context.browser.find_by_css('.btn').click()


@then('I see the login form')
def is_login_page(context):
    assert context.browser.is_element_present_by_css('.form-signin')


# Currently tests if login redirects to home page as I'm not sure how to test if user is authenticated
@then('I am successfully logged in and directed to the home page')
def is_logged_in(context):
    assert context.browser.url == context.get_url('/')


@then('I remain on the login page')
def on_login_page(context):
    assert context.browser.url == context.get_url('/login/')


@then('an error message \'{error_message}\' is displayed')
def error_message_displayed(context, error_message):
    assert context.browser.is_element_present_by_text(error_message)