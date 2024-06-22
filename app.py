from flask import Flask, render_template, request, url_for, redirect
from services import process
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/moodOption', methods=['POST'])
def getMood():
    mood = request.data
    global data
    data = process.processBackend(mood)
    return redirect(url_for("getPlaces"))
    
    
@app.route('/places')
def getPlaces():
    global data
    places = data.get("places", {})
    location = data.get("location", {})
    distanceMatrix = data.get("distanceMatrix", [])
    print(f"Location : {location} and Places : {distanceMatrix}")
    return render_template('placeTest.html', places=places.items(), location=location, distanceMatrix=distanceMatrix)

@app.route('/submitPhone', methods=['POST'])
def messagingMethod():
    process.processMessaging(request.data)
    print('Here')
    return redirect(url_for("home"))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, port=port)