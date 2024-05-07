import os
from notion_client import Client
import config

notion = Client()

import requests
from datetime import datetime, timezone

def extract_tables(page_url):
    # Get the page object
    page = notion.get_block(page_url)

    # Check if the page is a collection view
    if page['type'] != 'collection_view_page':
        print("Error: The provided page is not a collection view page.")
        return

    # Get the collection_id
    collection_id = page['parent']['id']

    # Get the collection data
    collection = notion.get_collection(collection_id)

    # Get the collection schema to map properties
    collection_schema = collection['schema']

    # Extract and print table data
    for view in page['view_ids']:
        table_data = notion.get_collection_view(view)
        for row in table_data['rows']:
            properties = {}
            for key, value in row['properties'].items():
                property_type = collection_schema[key]['type']
                # You can handle different property types here as needed
                if property_type == 'title':
                    properties[key] = value[0]['']
                elif property_type == 'text':
                    properties[key] = value[0]['']
                elif property_type == 'number':
                    properties[key] = value[0]['number']
                # Add more property type handling as required
            print("Row Properties:", properties)


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