import requests
from utilities.configurations import getConfig
from utilities.resources import ApiResources


def after_scenario(context, scenario):

    if "library_addbook" in scenario.tag:

        context.response6 = requests.delete('http://216.10.245.166/Library/DeleteBook.php',
                                            json={"ID": context.BookID},
                                            headers={"Content-Type": "application/json"})
        assert context.response6.status_code == 200
        expectedMsg = 'book is successfully deleted'
        deleteResponse = context.response6.json()
        assert expectedMsg == deleteResponse['msg']
        print(deleteResponse['msg'])
