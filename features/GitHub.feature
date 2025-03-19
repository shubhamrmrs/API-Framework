@functional
Feature: GitHub API validation

  @functional
  Scenario: (Positive) Get book details from Get_BookByAuthor API
    Given I have github auth credentials
    When I hit gitRepo API of Github
    Then status code of response should be 401