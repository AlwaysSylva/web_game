Feature: Login

Scenario: Go to the login page
    When I browse to http://127.0.0.1:8000/login
    Then I see the login page