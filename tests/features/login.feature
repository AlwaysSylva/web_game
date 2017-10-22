Feature: Login

Scenario: Go to login page
    When I browse to /login
    Then I see the login form

Scenario: Login with valid credentials
    Given a user 'user1' exists with password 'user1_password'
    When I browse to /login
    And login with username 'user1' and password 'user1_password'
    Then I am successfully logged in and directed to the home page