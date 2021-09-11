Feature: Text Input Feature

Scenario Outline: Validate Text Input
    Given I am at the UI Test Automation Playground
    And I navigate to Text Input test page
    When I input <text> on text input field
    And I press the Button that should change it's name based on input value
    Then The Button should have <text> in it

    Examples:
    |text|
    |any text|
    |welcome|