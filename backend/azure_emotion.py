
import requests
import os

PREDICTION_KEY = os.getenv('PREDICTION_KEY')
ENDPOINT = os.getenv('ENDPOINT')
PROJECT_ID = os.getenv('PROJECT_ID')
MODEL_NAME = os.getenv('MODEL_NAME')

def detect_emotion(image_bytes):
    url = f"{ENDPOINT}/customvision/v3.0/Prediction/{PROJECT_ID}/classify/iterations/{MODEL_NAME}/image"
    headers = {
        'Prediction-Key': PREDICTION_KEY,
        'Content-Type': 'application/octet-stream'
    }
    response = requests.post(url, headers=headers, data=image_bytes)
    response.raise_for_status()
    predictions = response.json().get('predictions', [])
    return predictions
