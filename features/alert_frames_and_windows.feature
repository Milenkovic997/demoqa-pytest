Feature: DemoQA Main Site

  Scenario: Validate Logo Active
    Given launch chrome
    When open website
    And verify logo present
    Then close browser