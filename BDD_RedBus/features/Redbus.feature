Feature: Redbus

  Scenario Outline: : user should be able to access tickets
    Given open the browser and enter the url
    When user is able to click on the manage bookings
    Then user is able to click on the show my tickets
    And user is able to enter data into the TICKET NUMBER textfield "<f_name>"
    And user is bale to enter data into the MOBILE NUMBER textfield "<l_name>"
    And user is able to click on submit
    And close browser

    Examples:
    | f_name       | l_name    |
    | TR9Q46783288 | 6301018116|
    | TRAJ63158961 | 9353781139|
    | TRA231990655 | 9353781139|
    | TR9781188747 | 9353781139|
    | TR9781188747 | Srikanth  |




