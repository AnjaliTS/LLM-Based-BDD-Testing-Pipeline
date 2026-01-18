Feature: E-commerce Shopping
  As a customer
  I want to purchase products online
  So that I can shop from home

  @positive @happy
  Scenario: Successful login and purchase
    Given I am on the login page
    When I enter "standard_user" as username
    And I enter "secret_sauce" as password
    And I click the login button
    Then I should be redirected to the products page
    And I should see "Products" header
    
    When I click "Add to Cart" on "Sauce Labs Backpack"
    And I click the shopping cart icon
    And I click "Checkout"
    And I enter "John" as first name
    And I enter "Doe" as last name
    And I enter "12345" as zip code
    And I click "Continue"
    And I click "Finish"
    Then I should see "Thank you for your order!"
    And the order should be completed successfully

  @positive @happy
  Scenario: Add multiple items to cart
    Given I am logged in as "standard_user"
    When I add "Sauce Labs Backpack" to cart
    And I add "Sauce Labs Bike Light" to cart
    Then the cart should show 2 items
    And the cart total should be $55.99

  @negative
  Scenario: Login with invalid credentials
    Given I am on the login page
    When I enter "invalid_user" as username
    And I enter "wrong_password" as password
    And I click the login button
    Then I should see "Username and password do not match" error
    And I should remain on the login page

  @negative
  Scenario: Checkout with empty cart
    Given I am logged in as "standard_user"
    And my shopping cart is empty
    When I click the shopping cart icon
    Then the "Checkout" button should be disabled
    And I should see "Your cart is empty" message