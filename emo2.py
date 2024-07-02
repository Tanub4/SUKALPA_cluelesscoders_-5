import cv2

# Define emotion zones based on relative positions of eyes and mouth (heuristic approach)
def detect_emotion(eye_y, mouth_y):
    emotion = ""
    if eye_y < mouth_y:  # Mouth is lower than eyes (potential for a smile)
        emotion_delta = mouth_y - eye_y
        if emotion_delta > 30:  # Wider gap suggests a big smile (Happy)
            emotion = "Happy"
        else:  # Smaller gap suggests a subtle smile (Neutral)
            emotion = "Neutral"
    elif eye_y > mouth_y:  # Mouth is higher than eyes (potential for a frown)
        emotion_delta = eye_y - mouth_y
        if emotion_delta > 30:  # Wider gap suggests a deep frown (Sad)
            emotion = "Sad"
        else:  # Smaller gap suggests a neutral expression (Neutral)
            emotion = "Neutral"
    else:  # Eyes and mouth at similar height (Neutral)
        emotion = "Neutral"
    return emotion

# Load pre-trained haar cascade for face detection
face_cascade = cv2.CascadeClassifier("C:\\Users\\navai\\Downloads\\haarcascade_frontalface_default.xml")

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

        # Extract eye and mouth regions (heuristic approach)
        eye_y = y + h // 3  # Approximate center of eye region
        mouth_y = y + (2 * h) // 3  # Approximate center of mouth region

        # Detect emotion using the improved function
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
