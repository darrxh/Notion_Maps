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

def find_restaurants(query):

    # Define parameters for nearby search
    params = {
        'location': 'latitude,longitude',  # Specify latitude and longitude coordinates
        'radius': 5000,  # Search within a 5000-meter radius
        'keyword': query  # Search for the provided query term (e.g., "restaurants")
    }

    # Perform nearby search
    places_result = gmaps.places_nearby(**params)

    # Extract relevant information from the results
    restaurants = []
    for place in places_result.get('results', []):
        name = place.get('name')
        address = place.get('vicinity')
        rating = place.get('rating', 'N/A')
        restaurants.append({'name': name, 'address': address, 'rating': rating})

    return restaurants

def find_top_result(query):
    # Define parameters for nearby search
    params = {
        'location': 'latitude,longitude',  # Specify latitude and longitude coordinates
        'radius': 5000,  # Search within a 5000-meter radius
        'keyword': query  # Search for the provided query term (e.g., "restaurants")
    }

    # Perform nearby search
    places_result = gmaps.places_nearby(**params)

    # Extract relevant information from the top result
    top_result = places_result.get('results', [])[0]  # Get the first result
    if top_result:
        place_id = top_result.get('place_id')
        details = gmaps.place(place_id=place_id,
                              fields=['name', 'formatted_address', 'rating', 'price_level', 'website',
                                      'opening_hours']).get('result')
        if details:
            name = details.get('name')
            address = details.get('formatted_address')
            rating = details.get('rating', 'N/A')
            price_level = details.get('price_level', 'N/A')
            website = details.get('website', 'N/A')
            opening_hours = details.get('opening_hours', {}).get('weekday_text', 'N/A')
            return {
                'name': name,
                'address': address,
                'rating': rating,
                'price_level': price_level,
                'website': website,
                'opening_hours': opening_hours
            }
    return None


query = input("Enter your query (e.g., 'restaurants'): ")
results = find_restaurants(query)

gmaps = googlemaps.Client(key=os.getenv("API_KEY"))

# Geocoding an address
geocode_result = gmaps.geocode("")

