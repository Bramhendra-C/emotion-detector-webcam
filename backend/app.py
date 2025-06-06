
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import os
from azure_emotion import detect_emotion

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        image_data = data.get('image')
        if not image_data:
            return jsonify({'error': 'No image provided'}), 400

        image_bytes = base64.b64decode(image_data.split(',')[1])
        emotions = detect_emotion(image_bytes)
        return jsonify({'emotions': emotions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
