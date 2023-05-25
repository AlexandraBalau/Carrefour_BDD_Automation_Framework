Feature: Check the home page functionality

  Background:
    Given home: I am on home page
    When  base: Close cookies popup

  @test_home_page
    Scenario: Verify home page url
        Then home: Check the url to be "https://carrefour.ro/"

  @home_page_return
    Scenario: Click logo button and return to home
        When home: I click Carrefour logo
        Then home: Check the url to be "https://carrefour.ro/"

  @cat_and_subcat
    Scenario Outline: Hovering over category and subcategory
      When home: I click the menu button
      When home: I hover over "<category>"
      Then home: I hover over "<subcategory>"

    Examples:
      | category              | subcategory |
      | Electrocasnice Mici   | Mic Dejun   |
      | Jocuri si Jucarii     | LEGO        |
