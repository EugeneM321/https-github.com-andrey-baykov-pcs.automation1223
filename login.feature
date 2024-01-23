Feature: Login tests

  Scenario: Verify login with valid credentials
    Given Navigate to "prod" environment
    Then Type "pcs.class1223@gmail.com" into field "Email"
    Then Type "Qwertyui1@" into field "password"
    Then Click on "//button[./span[text()='Login']]"
    Then Click on "//a[.//p[text()='Settings']]"
    Then Click on "//a[text()='Notifications']"
    Then Wait 2 seconds
    Then Revert switch "Off" of element "//button[@role='switch']"
    Then Wait 2 seconds

  Scenario: Verify privacy
    Given Navigate to "prod" environment
    Then Login as "Admin"
#    Then Type "pcs.class1223@gmail.com" into field "Email"
#    Then Type "Qwertyui1@" into field "password"
#    Then Click on "Login"
    Then Click on "Settings"
    Then Click on menu in settings "Privacy"
    Then Switch privacy for "Friends and relatives list" to "Only Me"
    Then Wait 2 seconds

  Scenario: Verify privacy admin
    Given Navigate to "prod" environment
    Then Login as "Admin"
    Then Click on "Settings"
    Then Click on menu in settings "Privacy"
    Then Switch privacy for "Friends and relatives list" to "Only Me"
    Then Wait 2 seconds

  Scenario: Verify privacy Manager
    Given Navigate to "prod" environment
    Then Login as "Manager"
    Then Click on "Settings"
    Then Click on menu in settings "Privacy"
    Then Switch privacy for "Feed" to "Only Me"
    Then Wait 2 seconds

#    pcs.class1223+2@gmail.com
#  Qwertyui2@

#    pcs.class1223+3@gmail.com
#  Qwertyui3@