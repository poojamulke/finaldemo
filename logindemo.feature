Feature: Wyscout Login

  Scenario: Login to Wyscout with valid credentials
    Given I Launch Chrome browser
    When I open Wyscout Homepage
    And Enter username"poojamulke77@gmail.com" and Password "pw_IndiaTest!"
    And Click on Sign_in button
    Then User must successfully login to the Wyscout Homepage
