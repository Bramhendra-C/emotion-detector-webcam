# Real-Time Emotion Detection with Azure Face API

This project implements real-time emotion detection using Azure Cognitive Services Face API and OpenCV. It captures video from a webcam, detects faces, and identifies emotions (e.g., happiness, sadness, anger) with confidence scores, displaying results in real-time.

## Features
- Captures live video feed using OpenCV.
- Detects faces and analyzes emotions using Azure Face API.
- Displays bounding boxes around faces with dominant emotion and confidence scores.
- Configurable via environment variables for secure API key management.

## Prerequisites
- *Azure Subscription*: An active Azure account with a Face API resource.
- *Python 3.x*: Installed on your system.
- *Webcam*: For real-time video capture.
- *Operating System*: Tested on Windows 10 (adaptable to other OS with minor changes).

## Setup Instructions

### 1. Azure Face API Setup
1. Create a Face API resource in the [Azure Portal](https://portal.azure.com).
2. Note the *API Key* and *Endpoint URL* from the resource's "Keys and Endpoint" section.

### 2. Install Dependencies
Install required Python libraries:
```bash
pip install azure-cognitiveservices-vision-face opencv-python

Open Environment Variables:Search for environment variables in the Start menu and select Edit environment variables for your account.Add new user variables:Variable Name: AZURE_FACE_API_KEY
Variable Value: Your Azure Face API key (e.g., your-api-key-here).Variable Name: AZURE_FACE_ENDPOINT
Variable Value: Your Azure endpoint URL (e.g., https://your-resource-name.cognitiveservices.azure.com/).Save and restart your IDE/terminal to apply changes.

emotion-detection-project/
│
├── emotion_detection.py  # Main script for real-time emotion detection
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies

python emotion_detection.py
