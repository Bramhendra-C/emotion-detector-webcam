
import React, { useRef, useState } from 'react';
import Webcam from 'react-webcam';
import axios from 'axios';

function App() {
  const webcamRef = useRef(null);
  const [emotion, setEmotion] = useState(null);

  const captureAndDetect = async () => {
    const imageSrc = webcamRef.current.getScreenshot();
    const res = await axios.post('http://localhost:5000/predict', { image: imageSrc });
    setEmotion(res.data.emotions);
  };

  return (
    <div className="App">
      <h1>Real-Time Emotion Detection</h1>
      <Webcam ref={webcamRef} screenshotFormat="image/jpeg" />
      <button onClick={captureAndDetect}>Detect Emotion</button>
      <pre>{JSON.stringify(emotion, null, 2)}</pre>
    </div>
  );
}

export default App;
