# coding: utf-8

import pyrebase
from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyCY2xmJQmxKVtV0kcyS9UccAWBDYAHMCv4",
    "authDomain": "meshimatch-47632.firebaseapp.com",
    "databaseURL": "https://meshimatch-47632.firebaseio.com",
    "projectId": "meshimatch-47632",
    "storageBucket": "meshimatch-47632.appspot.com",
    "messagingSenderId": "7175435560",
    "appId": "1:7175435560:web:32d216284133908a8ccc1d",
    "measurementId": "G-PKSJ0GG52X"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
# db.child("names").push({"name":"kota"})
# db.child("names").push({"name":"take"})

geo_request_url = 'https://get.geojs.io/v1/ip/geo.json'
geo_data = requests.get(geo_request_url).json()

# ルートを指定、メソッドはGET、POST
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('./index.html',lat = geo_data['latitude'], log=geo_data['longitude'])

@app.route('/result', methods=['POST'])
def result():
    render_template('./result.html')

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
