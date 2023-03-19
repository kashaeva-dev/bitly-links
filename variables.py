import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

token = os.getenv('BITLY_TOKEN')
group_guid = os.getenv('GROUP_GUID')