import json

def processBackend(data):
    jsonString = data.decode('utf-8')
    jsonData = json.loads(jsonString) 
   
    lat, long, mood = jsonData
    
    
    
    print (jsonData[long])
    
    
    
def promptResponse(city):
    