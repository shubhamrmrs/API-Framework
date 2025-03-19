@functional
Feature: Post And Delete API Features

  @library_addbook
  @smoke
  Scenario: (Positive) Add book details using Add_Book Post API
    When send post request using Add_Book API
    Then validate response code, response type, response header of Add_Book API
    Then validate response body of Add_Book API
    Then Retrieve Id from response body of Add_Book API

  @library_addbook
  @smoke
  Scenario: (Positive) Add book details using Add_Book Post API (for existing aisle)
    When send post request using Add_Book API2
    Then validate response code of Add_Book API2
    Then validate response body of Add_Book API2

#  @functional
#  Scenario: (Positive) Delete book details using Delete_Book Post API
#    When send post request using Delete_Book API
#    Then validate response code of Delete_Book API
#    Then validate msg of response body of Delete_Book API
#
  @smoke
  Scenario: (Negative) Delete book details using Delete_Book Post API for incorrect ID
    When send post request using Delete_Book API2
    Then validate response code, response type, response header of Delete_Book API2
    Then validate msg of response body of Delete_Book API2

  @library_addbook
  @regression
  Scenario Outline: (Positive) Add book details using Add_Book Post API
    When send post request using "<isbn>" and "<aisle>"
    Then validate response code, response type of Add_Book APIs
##    Then validate response body of Add_Book API
##    Then Retrieve Id from response body of Add_Book API
    Examples:
      |isbn  |aisle |
      | fefssws |  94238775  |
     | erwedsce |  94238775 |
      | fefasws |  94238775  |
     | erwesdscse |  94238775 |
      | fefsxsws |  94238775  |
     | erwaxedsce |  94238775 |
      | fefsaxasws |  94238775  |
     | erwesadsce |  94238775 |
      | fefssws |  94238775  |
     | erwesdsce |  94238775 |