Feature: Login

Scenario: Go to login page
    When I browse to /login
    Then I see the login form

Scenario: Login with valid credentials
    Given a user 'user1' exists with password 'user1_password'
    When I browse to /login
    And login with username 'user1' and password 'user1_password'
    Then I am successfully logged in and directed to the home page

Scenario: Login with invalid credentials
    Given a user 'user1' exists with password 'user1_password'
    When I browse to /login
    And login with username 'user1' and password 'user2_password'
    Then I remain on the login page
    And an error message 'Your username and password didn't match. Please try again.' is displayed