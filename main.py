import config

DATABASE_ID = "Spots-66f3a67b298140eb9e81e696fac300d5?pvs=4"
import requests
from datetime import datetime, timezone


headers = {
    "Authorization": "Bearer " + config.API_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}


def get_pages():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    payload = {"page_size": 100}
    response = requests.post(url,json=payload,headers=headers)

    data = response.json