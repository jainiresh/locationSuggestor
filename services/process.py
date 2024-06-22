import json
from services import openCageData
from services import geminiAi
from services import twilioService
import services
import services.googleMapsService
import asyncio

def processMessaging(data):
    jsonData = eval(data)
    print(jsonData)
    # {'phoneNumber': '9095315305',
    #  'placeTitle': 'Koodal Azhagar Temple',
    #  'location': {'city': 'Madurai',
    #               'state': 'Tamil Nadu',
    #               'country': 'India',
    #               'lat' : xx,
    #               'long': xx
    # }
    #  }
    locData = jsonData['location']
    link = services.googleMapsService.getMapLink(locData['lat'], locData['long'], f"{jsonData['placeTitle']},{locData['city']},{locData['state']},{locData['country']}")

    contentToConsumer = f"Click on this link to get started towards {jsonData['placeTitle']}"
    response = twilioService.createMessage(jsonData['phoneNumber'], contentToConsumer + " : " + link)
    print( f"Twilio response: {response}")
    return "ok"
    
def processBackend(data):
    jsonString = data.decode('utf-8')
    jsonData = json.loads(jsonString) 
   
    lat, long, mood = jsonData
    
    city, state, country = openCageData.get_location_info(jsonData[lat], jsonData[long])
    
    response = geminiAi.getResponseForPrompt(city, state, country, jsonData[mood])
    
    response = response.replace("```json","")
    response = response.replace("```","")
    response = eval(response)
    
    locationObj = {}
    locationObj['city'] = city
    locationObj['state'] = state
    locationObj['country'] = country
    locationObj['lat'] = jsonData[lat]
    locationObj['long'] = jsonData[long]
    
    finalObj = {}
    finalObj['places'] = response
    finalObj['location'] = locationObj
    
    
    distanceMatrix = []
    
    for place, description in response.items():
        dest = f"{place},{city},{state},{country}"
        distanceMatrix.append(
            services.googleMapsService.getDistanceMatrix(jsonData[lat], jsonData[long], dest)
        )
    finalObj['distanceMatrix'] = distanceMatrix
    
    # finalObj = {
    #     places: {
    #         place1:desc1,
    #         place2:desc2
    #     },
    #     distanceMatrix: [{
    #         distance:"",
    #         time:""
    #     }]
    #     location:{
    #         city:,
    #         state:,
    #         country:,
    #         lat:,
    #         long:
    #     }
    # }
    
    print(f"Response from prompt : {response}")
    return finalObj
    
    
    
    