import googlemaps
from datetime import datetime
from urllib.parse import quote
from config.googleApiCreds import google_direction_matrix_api_key


gmapsForDistanceMatrix = googlemaps.Client(key=google_direction_matrix_api_key)

def getMapLink(lat, long, destinationAddress):
    base_url = "https://www.google.com/maps"
    
    return f"{base_url}?saddr={lat},{long}&daddr={quote(destinationAddress)}"

def getDistanceMatrix(lat, long, destinationAddress):
    source = f"{lat},{long}"
    response = gmapsForDistanceMatrix.distance_matrix(source,destinationAddress)
    responseObj =  {
        "distance": response['rows'][0]['elements'][0]['distance'],
        "time": response['rows'][0]['elements'][0]['duration']
    }
    return responseObj
    
    
