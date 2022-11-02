Feature: Friends

  Scenario Outline: User should able to search and add friends in the application successfully
    Given Open the browser and enter the valid url
    When Enter the Username"<username_>"
    And Enter the Password"<pwd>"
    And Click on login button


    And Click on friends button
#    And Click on new message button
    And Click on friend request button
    And Click on confirm request
    And Click on sent request link
    And Click on delete request

#
#    And Click on suggestion button
#    And Click on add friend button
#    And Click on remove friend button
#
#
#    And Click on all friend button
#    And Click on search bar
#    And Click on search dot
#    And Click on message button
#    And Click on block button
#    And Click on unfriend button
#
#
#    And Click on Birthday button
#    And Click on name link
#
#
#    And Click on custom list
#    And Click on close friend button
#    And Click on fav button
#    And Click on frds button
#
#    And Click on notification settings button
#    And Click on notification dot button
    Then Close the browser


    Examples:
      | username_                    | pwd        |
      | jadhavsanjana1975@gmail.com | Cartoon#98 |





