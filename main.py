import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv, find_dotenv


def shorten_link(url, token):
    request_url = 'https://api-ssl.bitly.com/v4/shorten'

    headers = {
       'Authorization': token,
    }

    params = {
        "long_url": url,
    }

    response = requests.post(request_url, headers=headers, json=params)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(url, token):
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


def is_bitlink(url, token):
    request_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}'

    headers = {
        'Authorization': token,
    }

    response = requests.get(request_url, headers=headers)
    return response.ok


def create_parser():
    parser = argparse.ArgumentParser(
        prog='Bitlinks',
        description='A Python wrapper for the Bitly API, which can be used '
                    'to shorten URLs and track clicks on shortened links',
    )
    parser.add_argument('url', help='Необходимо ввести ссылку')
    return parser


def main():
    load_dotenv(find_dotenv())

    try:
        token = os.environ['BITLY_TOKEN']
    except KeyError:
        print("Не получается найти переменную окружения BITLY_TOKEN")

    parser = create_parser()
    user_input = parser.parse_args()

    url = user_input.url
    parsed_url = urlparse(url)
    cropped_url = "".join([parsed_url.netloc, parsed_url.path])

    if is_bitlink(cropped_url, token):
        print(f"По Вашей ссылке прошли: {count_clicks(cropped_url, token)} раз(а)")
    else:
        print(f"Битлинк: {shorten_link(url, token)}")


if __name__ == "__main__":
    main()
