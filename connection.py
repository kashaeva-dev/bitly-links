import requests
import json
import os

token = os.environ.get('BITLY_TOKEN')
group_guid = os.environ.get('BITLY_GROUP_GUID')


def get_user_info(token=token):
    url = 'https://api-ssl.bitly.com/v4/user'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }
    response = requests.get(url, headers=headers)
    return response.text


def print_user_info(response_text):
    user_info = json.loads(get_user_info())
    for key, value in user_info.items():
        print(key, value, sep=': ')


print_user_info(get_user_info())