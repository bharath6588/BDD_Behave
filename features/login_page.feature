Feature: Login Feature

  Scenario: Verify valid user
    Given provide valid username
    When provide valid password
    And click login button
    Then verify home page header text as swag labs