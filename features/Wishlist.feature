#Wishlist product in Flipkart

  Feature: wishlist flipkart
    Scenario Outline: wishlist the product in to flipkart
      Given We are on flipkart website
      Then Enter your "<username>" in the feild
      And Enter your "<password>" in the box
      And Click login
      Then Type "<searchTEXT>" in search bar
      And Click on search button
      Then Click on the wishlist button
      And Click on the username
      And Click on the wishlist from the option listed
      Then Check the product is in the wishlist
      And Click on the wishlist product
      Then Verify the product
      And Close the tab
      Then Click on the delete button
      And Click on the yes remove

      Examples:
        | username | password | searchTEXT |
        | vaishnavigulwe1307@gmail.com | Vaish@1307 | samsung a73 5g |
        | vaishnavigulwe1307@gmail.com | Vaish@1307 | oppo f19 pro   |
#        | vaishnavigulwe1307@gmail.com | Vaish@1307 | noise evolve 3 |




