import requests

def get_location_info(latitude, longitude, api_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get('results', [])
        if results:
            address_components = results[0].get('address_components', [])
            city = None
            state = None
            for component in address_components:
                if 'locality' in component['types']:
                    city = component['long_name']
                if 'administrative_area_level_1' in component['types']:
                    state = component['long_name']
            return city, state
    return None, None

# Example usage
latitude = 9.945088
longitude = 78.135296
api_key = 'AIzaSyCFIFw8X7OTSOJ5lh-Z-HUxzNzbD2TYl-w'
city, state = get_location_info(latitude, longitude, api_key)
print(f"City: {city}, State: {state}")