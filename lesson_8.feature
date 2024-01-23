Feature: Lesson 8

  Background:
    Given Navigate to "prod" environment


  Scenario: Verify privacy admin
    Then Login as "Admin"
    Then Click on "Settings"
    Then Click on menu in settings "Privacy"
    Then Switch privacy for "Friends and relatives list" to "Only Me"
    Then Wait 2 seconds

  Scenario: Verify privacy Manager
    Then Login as "Manager"
    Then Click on "Settings"
    Then Click on menu in settings "Privacy"
    Then Switch privacy for "Friends and relatives list" to "Only Me"
    Then Wait 2 seconds


  Scenario: Verify privacy Manager with table
    Then Login as "Manager"
    Then Click on "Settings"
    Then Click on menu in settings "Privacy"
    Then Switch privacy
      | group                      | level   |
      | Friends and relatives list | Public  |
      | Feed                       | Public  |
      | Family Tree                | Public  |
      | About information          | Public  |
      | Location                   | Only Me |
      | Photos                     | Public  |
      | Videos                     | Public  |
    Then Wait 2 seconds

  Scenario Outline: Verify logins
    Then Login with credentials username "<email>" password "<password>" result "<result>"
    Then Wait 2 seconds

    Examples:
      | email                     | password   | result |
      | pcs.class1223@gmail.com   | Qwertyui1@ | true   |
#      | pcs.class1223+2@gmail.com | Qwertyui2@ | true   |
#      | pcs.class1223+3@gmail.com | Qwertyui3@ | true   |
#      | pcs.class1223+4@gmail.com | Qwertyui4@ | false  |


  Scenario: Click google play
    Then Click google play button
    Then Wait 3 seconds