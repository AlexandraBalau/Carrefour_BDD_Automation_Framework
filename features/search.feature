Feature: Carrefour search feature

    Background:
      Given home: I am on home page

    @search
    Scenario Outline: Test search functionality
      When home: I search after "<query>"
      Then home: I click search button
      Then products: I verify that results contain search query "<query>"

    Examples:
      | query    |
      | televizor|
      | iphone   |
      | samsung  |