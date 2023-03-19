import json

import requests

from variables import token, group_guid


def shorten_link(url=input("Введите ссылку, которую хотите сократить: "), token=token, group_guid=group_guid):
    request_url = 'https://api-ssl.bitly.com/v4/shorten'

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }

    data = {
        "long_url": url,
        "domain": "bit.ly",
        "group_guid": group_guid,
    }

    data_json = json.dumps(data)
    response = requests.post(request_url, headers=headers, data=data_json)
    response.raise_for_status()
    return response.json()['id']


print('Битлинк', shorten_link())
