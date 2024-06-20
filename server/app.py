from flask import Flask, request, jsonify
from flask_cors import CORS 
from pymongo import MongoClient
from dotenv import load_dotenv

import os

load_dotenv()

app = Flask(__name__)
CORS(app)

client = MongoClient(os.getenviron.get('MONGO_URI'))
db = client.database

if __name__ == '__main__':
    app.run(debug=True)

