from flask import Flask, request, jsonify
from flask_cors import CORS 
from pymongo import MongoClient
from dotenv import load_dotenv

import requests
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

client = MongoClient(os.environ.get('MONGO_URI'))

API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/api/fetch_weather', methods=['GET'])
def fetch_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City is required"})
    
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'imperial' #imperial units for right now
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        return jsonify({"error": data.get("message", "Error fetching data")}), response.status_code
    
    weather = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"]
    }

    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True)
