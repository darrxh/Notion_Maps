import os
from notion_client import Client
import config


import requests
from datetime import datetime, timezone



def get_pages():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    payload = {"page_size": 100}
    response = requests.post(url,json=payload,headers=headers)
    data = response.json
    pass


def get_token():
    txt_object = open("api.txt", "r")
    api_token = txt_object.read()
    txt_object.close()
    return api_token


def main():
    api_key = get_token()
    notion = Client(auth=api_key)
    print (notion.users.list())

main()