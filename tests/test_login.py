from pytest_bdd import scenarios, when, then, parsers

scenarios('features')

@when(parsers.parse('I browse to {site}'))
def go_to_url(site, browser):
    browser.visit(site)

@then('I see the login page')
def is_login_page(browser):
    browser.find_by_css('.form-signin').first