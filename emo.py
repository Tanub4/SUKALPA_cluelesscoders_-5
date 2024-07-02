import cv2

# Define emotion zones (replace with actual emotion detection logic)
def detect_emotion(eye_y, mouth_y):
  if eye_y > mouth_y:
    return "Happy"
  elif eye_y < mouth_y:
    return "Sad"
  else:
    return "Neutral"

# Load pre-trained haar cascade for face detection
face_cascade = cv2.CascadeClassifier("C:\\Users\\navai\\Downloads\\haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier("C:\\Users\\navai\\Downloads\\haarcascade_smile.xml")

# Start video capture
cap = cv2.VideoCapture(0)

while True:
  # Read frame from camera
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Detect faces
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

  # Process each detected face
  for (x, y, w, h) in faces:
    # Draw rectangle around the face
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Extract eye and mouth regions (replace with actual eye/mouth detection)
    eye_y = y + h // 3
    mouth_y = y + h // 2

    # Detect emotion
    emotion = detect_emotion(eye_y, mouth_y)

    # Display emotion text on frame
    cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

  # Display resulting frame
  cv2.imshow('Emotion Detection', frame)

  # Exit on 'q' key press
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# Release resources
cap.release()
cv2.destroyAllWindows()

