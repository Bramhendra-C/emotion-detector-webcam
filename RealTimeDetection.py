import cv2
import os
from io import BytesIO
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

# Azure Face API credentials (read from environment variables)
ENDPOINT = os.getenv("AZURE_FACE_ENDPOINT")
KEY = os.getenv("AZURE_FACE_API_KEY")

# Ensure credentials are set
if not ENDPOINT or not KEY:
    raise ValueError("Azure Face API key or endpoint not found in environment variables.")

# Initialize FaceClient
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Helper function to extract dominant emotion
def get_dominant_emotion(emotion):
    emotions = {
        'anger': emotion.anger,
        'contempt': emotion.contempt,
        'disgust': emotion.disgust,
        'fear': emotion.fear,
        'happiness': emotion.happiness,
        'neutral': emotion.neutral,
        'sadness': emotion.sadness,
        'surprise': emotion.surprise
    }
    dominant = max(emotions, key=emotions.get)
    return dominant, round(emotions[dominant], 2)

# Start real-time detection
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Encode frame to JPEG and wrap in BytesIO for Azure API
    ret, buffer = cv2.imencode('.jpg', frame)
    if not ret:
        print("Error: Failed to encode frame.")
        continue

    frame_stream = BytesIO(buffer.tobytes())

    # Detect faces with emotion attributes
    try:
        detected_faces = face_client.face.detect_with_stream(
            image=frame_stream,
            return_face_attributes=['emotion']
        )

        for face in detected_faces:
            emotion = face.face_attributes.emotion
            name, confidence = get_dominant_emotion(emotion)

            # Draw rectangle around the face
            rect = face.face_rectangle
            left, top, width, height = rect.left, rect.top, rect.width, rect.height
            cv2.rectangle(frame, (left, top), (left + width, top + height), (0, 255, 0), 2)

            # Display emotion label
            label = f"{name}: {confidence}"
            cv2.putText(frame, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)

    except Exception as e:
        print(f"Error detecting faces: {e}")

    # Show the result
    cv2.imshow("Real-Time Emotion Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
