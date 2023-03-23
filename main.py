import json

import requests

from variables import token, group_guid
from urllib.parse import urlparse


def shorten_link(url, token=token, group_guid=group_guid):
    try:
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
    except requests.exceptions.HTTPError:
        return "Ошибка! Сервис Bitly недоступен."


def count_clicks(url, token=token):

    try:
        request_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary'

        headers = {
            'Authorization': token,
        }

        params = {
            ('unit', 'day'),
            ('units', '-1'),
        }

        response = requests.get(request_url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()['total_clicks']

    except requests.exceptions.HTTPError:
        return "Ошибка! Сервис Bitly недоступен."


def is_bitlink(url):
    url_parsed = urlparse(url)
    return url_parsed.path.split('/')[0] == 'bit.ly'


if __name__ == "__main__":
    url = input('Введите ссылку: ')
    if is_bitlink(url):
        print(count_clicks(url))
    else:
        print(shorten_link(url))
