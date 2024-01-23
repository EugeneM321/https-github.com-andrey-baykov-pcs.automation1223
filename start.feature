Feature: Start page tests
  All tests for the start page

  Scenario: Verify start page
    Given Navigate to "https://www.lifetwig.com/"
    Then Wait 2 seconds
    When Verify login page is displayed


