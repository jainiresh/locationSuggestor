from flask import Flask, render_template, request
from services import process

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/moodOption', methods=['POST'])
def getMood():
    mood = request.data
    process.processBackend(mood)
    return mood

if __name__ == '__main__':
    app.run(debug=True)