import json

import requests

from variables import token, group_guid


def shorten_link(token=token, group_guid=group_guid):
    url = input("Введите ссылку, которую хотите сократить: ")
    try:                                                  # Проверяем, что пользователем была введена корректная ссылка
        requests.get(url)
    except requests.exceptions.ConnectionError:
        return "Ошибка! Введена неверная ссылка."

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


def count_clicks(token=token):
    url = input("Введите битлинк, для которого хотите узнать количество кликов: ")
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


print(count_clicks())
