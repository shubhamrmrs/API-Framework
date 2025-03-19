import requests
from behave import *
from utilities.configurations import getPassword
from utilities.resources import ApiResources


class GitHubApiTest:

    @given(u'I have github auth credentials')
    def step_impl(context):
        context.se = requests.session()
        context.se.auth = ('shubhamrmrs@gmail.com', getPassword())

    @when(u'I hit gitRepo API of Github')
    def step_impl(context):
        context.response = context.se.get(ApiResources.GitHubRepo)

    @then(u'status code of response should be {statusCode:d}')
    def step_impl(context,statusCode):
        assert context.response.status_code == statusCode
        print(context.response.status_code)
