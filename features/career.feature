Feature: Check the career location search functionality

  Background:
    Given home: I am on home page
    When  base: Close cookies popup


  @job_search
  Scenario Outline: Searching a job
    When career: I click career link
    When career: I search after "<city>"
    Then career: I search after "<store>"
    Then career: I click search job button


  Examples:
      | city             | store                   |
      | Iasi             | Carrefour Iasi Felicia  |
      | Brasov           | Carrefour Brasov        |