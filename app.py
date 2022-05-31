from flask import Flask
from datetime import datetime
import logging

app = Flask(__name__)

@app.route("/")
def hello():

    logging.info(str({'timestamp': str(datetime.now()), 'message': 'A thing happened'}))

    return {
        "Temp": 50,
        "Conditions": "Cloudy"
    }