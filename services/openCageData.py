import requests
import re
from config.openCageCreds import openCageApiKey

api_key = openCageApiKey
def get_location_info(latitude, longitude):
    url = f"https://api.opencagedata.com/geocode/v1/json?key={api_key}&q={latitude}%2C+{longitude}&pretty=1&no_annotations=1"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()['results'][0]['components']
        if results:
            city = results['city']
            state = results['state']
            country = results['country']
            print (f"Formatted address : {city}, {state}, {country}")
            return city, state, country
    return None, None, None
