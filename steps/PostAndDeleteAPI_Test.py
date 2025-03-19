import requests
from behave import *
from utilities.configurations import getConfig
from utilities.payload import addBookPayload
from utilities.resources import ApiResources


# PostAndDelete_API.feature
class PostApiTest:

    # (Positive) Add book details using Add_Book Post API
    @when(u'send post request using Add_Book API')
    def step_impl(context):
        url = getConfig()['API']['endpoint'] + ApiResources.Addbook
        headers = {"Content-Type": "application/json"}
        context.response = requests.post(url, json=addBookPayload('xsdsfdacd', 9411875), headers=headers)

    @then(u'validate response code, response type, response header of Add_Book API')
    def step_impl(context):
        assert context.response.status_code == 200
        print(context.response.status_code)

        context.json_response = context.response.json()
        print(type(context.json_response))

        response_headers = context.response.headers
        assert response_headers['Content-Type'] == 'application/json;charset=UTF-8'
        print(context.response.headers)

    @then(u'validate response body of Add_Book API')
    def step_impl(context):
        print(type(context.json_response))
        print(context.json_response['ID'])
        print(context.json_response['Msg'])

    @then(u'Retrieve Id from response body of Add_Book API')
    def step_impl(context):
        context.BookID = context.json_response['ID']
        print(context.BookID)
        # assert 1190904557778" == context.BookID

    # (Positive) Add book details using Add_Book Post API (for existing aisle)
    @when(u'send post request using Add_Book API2')
    def step_impl(context):
        url = getConfig()['API']['endpoint'] + ApiResources.Addbook
        headers = {"Content-Type": "application/json"}
        context.response = requests.post(url, json=addBookPayload('xsdsfdacd', 9411875), headers=headers)

    @then(u'validate response code of Add_Book API2')
    def step_impl(context):
        assert context.response.status_code == 200
        print(context.response.status_code)

    @then(u'validate response body of Add_Book API2')
    def step_impl(context):
        expectedMessage2 = "Book Already Exists"
        json_response = context.response.json()
        print(json_response)
        actualMessage2 = json_response['Msg']
        print(json_response['Msg'])
        assert expectedMessage2 == actualMessage2

    # (Positive) Delete book details using Delete_Book Post API
    # @when(u'send post request using Delete_Book API')
    # def step_impl(context):
    #     url2 = getConfig()['API']['endpoint'] + ApiResources.DeleteBook
    #     context.response = requests.delete(url2, json={"ID": context.BookID})
    #
    # @then(u'validate response code of Delete_Book API')
    # def step_impl(context):
    #     assert context.response.status_code == 200
    #     print(context.response.status_code)

    # @then(u'validate msg of response body of Delete_Book API')
    # def step_impl(context):
    #     expectedMsg = 'book is successfully deleted'
    #     deleteResponse = context.response.json()
    #     print(type(deleteResponse))
    #     print(deleteResponse['msg'])
    #     assert expectedMsg == deleteResponse['msg']

    # (Negative) Delete book details using Delete_Book Post API for incorrect ID
    @when(u'send post request using Delete_Book API2')
    def step_impl(context):
        url2 = getConfig()['API']['endpoint'] + ApiResources.DeleteBook
        context.response = requests.delete(url2, json={"ID": ""})

    @then(u'validate response code, response type, response header of Delete_Book API2')
    def step_impl(context):
        assert context.response.status_code == 404
        print(context.response.status_code)

    @then(u'validate msg of response body of Delete_Book API2')
    def step_impl(context):
        expectedMsg = 'Delete Book operation failed, looks like the book doesnt exists'
        deleteResponse = context.response.json()
        print(type(deleteResponse))
        print(deleteResponse['msg'])
        assert expectedMsg == deleteResponse['msg']

    @when(u'send post request using {isbn} and {aisle}')
    def step_impl(context, isbn, aisle):
        url = getConfig()['API']['endpoint'] + ApiResources.Addbook
        headers = {"Content-Type": "application/json"}
        context.response = requests.post(url, json=addBookPayload(isbn, aisle), headers=headers)


    @then(u'validate response code, response type of Add_Book APIs')
    def step_impl(context):
        assert context.response.status_code == 200
        print(context.response.status_code)

        context.response = context.response.json()
        print(type(context.response))

