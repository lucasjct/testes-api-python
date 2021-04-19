import json
import requests


def test_api_post():
    url = "http://dummy.restapiexample.com/api/v1"

    headers = {
        "Accept": "*/*",
        "User-Agent": "request",
        "Content-Type": "application/json",
    }

    endpoint = "/create"

    payload = {"name": "test", "salary": "123", "age": "23"}

    response = requests.post(
        url=url + str(endpoint), headers=headers, data=json.dumps(payload)
    )
    response_dict = response.json()

    if response.status_code == 200:
        status = response_dict["status"]
        content = len(response_dict["data"])

        assert status == "success" and content > 1
    else:
        False
