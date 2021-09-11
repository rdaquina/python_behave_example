Feature: Progress Bar Feature

Scenario Outline: Validate Progress Bar
    Given I am at the UI Test Automation Playground
    And I navigate to Progress Bar test page
    When I click the Start Progress Bar button
    And The Progress Bar is at <progressbar>
    Then I click on the Stop Progress Bar button
    And Result should be <result>

    Examples:
    |progressbar| result|
    |75%        | 123   |
    |50%        | 0     |
    |66%        | 0     |