import googlemaps
from datetime import datetime
from dotenv import load_dotenv, set_key

def load_env():
    try:
        open(".env","r")
    except FileNotFoundError:
        print ("No .env API key file given.")
        user_input = str(input("Please enter an API Key. For help or more information please refer to Documentation: \n"))
        new_key_file = open(".env","x")
        new_key_file.write(f"API_KEY={user_input}\nPREFIX=+")
        new_key_file.close()
    finally:
        load_dotenv()


gmaps = googlemaps.Client(key=os.getenv("API_KEY"))

# Geocoding an address
geocode_result = gmaps.geocode("")

