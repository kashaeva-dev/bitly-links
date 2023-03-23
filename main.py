import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv, find_dotenv


def shorten_link(url, token):
    try:
        request_url = 'https://api-ssl.bitly.com/v4/shorten'

        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
        }

        data = {
            "long_url": url,
            "domain": "bit.ly",
        }

        response = requests.post(request_url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['id']
    except requests.exceptions.HTTPError:
        return "Ошибка! Сервис Bitly недоступен."


def count_clicks(url, token):

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

    load_dotenv(find_dotenv())

    try:
        token = os.environ['BITLY_TOKEN']
        url = input('Введите ссылку: ')
        if is_bitlink(url):
            print(count_clicks(url, token))
        else:
            print(shorten_link(url, token))
    except KeyError:
        print("Не получается найти переменную окружения BITLY_TOKEN")
