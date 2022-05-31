from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():

    print({'timestamp': str(datetime.now()), 'message': 'A thing happened'})

    return {
        "Temp": 50,
        "Conditions": "Cloudy"
    }