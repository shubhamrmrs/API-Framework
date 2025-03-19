@functional
Feature: Get API Features

#  Background:
#    Given launch chrome browser and open url

  @functional
  Scenario: (Positive) Get book details from Get_BookByAuthor API
    When send get requtest to Get_BookByAuthor API
    Then validate response code, response type, response header of Get_BookByAuthor API
    Then validate response body of Get_BookByAuthor API
    Then validate book name as per index
#    Then Retrieve the book details with ISBN details

  @functional
  Scenario: (Positive) Get book details from Get_BookById API
    When send get requtest to Get_BookById API
    Then validate response code, response type of Get_BookById API
    Then validate response body of Get_BookById API

  @functional
  Scenario: (Negative) Get book details from Get_BookByAuthor API when using incorrect query parameter
    When send get requtest to Get_BookByAuthor API(N)
    Then validate response code of Get_BookByAuthor API(N)

  @functional
  Scenario: (Negative) Get book details from Get_BookById API when using incorrect query parameter
    When send get requtest to Get_BookById API(N)
    Then validate response code of Get_BookById API(N)
    Then validate response body of Get_BookById API(N)
