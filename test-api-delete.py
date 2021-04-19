import requests
import json


def test_api_delete():

    url = "http://dummy.restapiexample.com/api/v1/delete/"

    headers = {
        "Accept": "*/*",
        "User-Agent": "request",
        "Content-Type": "application/json",
    }

    id = 83

    response = requests.delete(url=url + str(id), headers=headers)

    assert response.status_code == 200
