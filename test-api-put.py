import requests
import json


def test_api_put():

    url = "http://dummy.restapiexample.com/api/v1/update/"

    headers = {
        "Accept": "*/*",
        "User-Agent": "request",
        "Content-Type": "application/json",
    }
    # caso houver atenticação, ela deve ser passada através do header.

    id = 83

    payload = {"name": "Cristina", "salary": "125", "age": "23"}

    response = requests.put(
        url=url + str(id), headers=headers, data=json.dumps(payload)
    )

    response_dict = response.json()

    if response.status_code == 200:
        status = response_dict["status"]
        content = len(response_dict)
        assert status == "success" and content > 1
    else:
        False
