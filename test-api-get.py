import json
import requests


def test_exemplo_get():

    auth = ""
    url = "http://dummy.restapiexample.com/api/v1"

    headers = {
        "Accept": "*/*",
        "User-Agent": "request",
    }  # Sempre devo passar o cabeçalho da requisição

    endpoint = "/employees"

    # payload = {''}
    response = requests.get(url=url + str(endpoint), headers=headers)
    response_dict = response.json()
    status = response_dict["status"]

    if response.status_code == 200:
        status = response_dict["status"]
        conteudo = response_dict["data"]

        assert status == "success" and len(conteudo) > 0
    else:
        False
