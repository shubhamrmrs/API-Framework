import requests
from behave import *
from utilities.configurations import getConfig
from utilities.payload import addBookPayload
from utilities.resources import ApiResources

# Get_API.feature
class GetApiTest:

    # (Positive) Get book details from Get_BookByAuthor API
    @when(u'send get requtest to Get_BookByAuthor API')
    def step_impl(context):
        context.response = requests.get('http://216.10.245.166//Library/GetBook.php',
                                        params={'AuthorName': 'Rahul Shetty2'})

    @then(u'validate response code, response type, response header of Get_BookByAuthor API')
    def step_impl(context):
        assert context.response.status_code == 200
        print(context.response.status_code)

        context.json_response = context.response.json()
        print(type(context.json_response))

        response_headers = context.response.headers
        assert response_headers['Content-Type'] == 'application/json;charset=UTF-8'
        print(context.response.headers)

    @then(u'validate response body of Get_BookByAuthor API')
    def step_impl(context):
        print(context.json_response)

    @then(u'validate book name as per index')
    def step_impl(context):
        print(context.json_response[0]['book_name'])

    # # @then(u'Retrieve the book details with ISBN details')
    # # def step_impl(context):
    # #     expectedBook =  {
    # #         "book_name": "Learn Appium Automation with Java",
    # #         "isbn": "bcz888dfseded",
    # #         "aisle": "20027" }
    # #
    # # for book in context.json_response:
    # #     if book['isbn'] == 'bcz888dfseded':
    # #         actualBook = book
    # #         assert expectedBook == actualBook
    #
    # (Positive) Get book details from Get_BookById API
    @when(u'send get requtest to Get_BookById API')
    def step_impl(context):
        context.response = requests.get('http://216.10.245.166//Library/GetBook.php',
                                         params={'ID': 'bcd57779'})

    @then(u'validate response code, response type of Get_BookById API')
    def step_impl(context):
        assert context.response.status_code == 200
        print(context.response.status_code)

        context.json_response = context.response.json()
        print(type(context.json_response))

    @then(u'validate response body of Get_BookById API')
    def step_impl(context):
        print(context.json_response)

    # (Negative) Get book details from Get_BookByAuthor API when using incorrect query parameter
    @when(u'send get requtest to Get_BookByAuthor API(N)')
    def step_impl(context):
        context.response = requests.get('http://216.10.245.166//Library/GetBook.php',
                                         params={'AuthorName': ''})

    @then(u'validate response code of Get_BookByAuthor API(N)')
    def step_impl(context):
        assert context.response.status_code == 500
        print(context.response.status_code)

    # (Negative) Get book details from Get_BookById API when using incorrect query parameter
    @when(u'send get requtest to Get_BookById API(N)')
    def step_impl(context):
        context.response = requests.get('http://216.10.245.166//Library/GetBook.php',
                                         params={'ID': ''})

    @then(u'validate response code of Get_BookById API(N)')
    def step_impl(context):
        assert context.response.status_code == 404
        print(context.response.status_code)

    @then(u'validate response body of Get_BookById API(N)')
    def step_impl(context):
        expectedMessage = "The book by requested bookid / author name does not exists!"
        json_response = context.response.json()
        print(json_response)
        actualMessage = json_response['msg']
        print(json_response['msg'])
        assert expectedMessage == actualMessage

