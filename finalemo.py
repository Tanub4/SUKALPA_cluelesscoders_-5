import cv2
import time

# Define emotion zones based on relative positions (heuristic approach)
def detect_emotion(eye_y, mouth_y):
    emotion = ""
    emotion_delta = mouth_y - eye_y
    if emotion_delta > 30:  # Wider gap suggests a smile (Happy)
        emotion = "Happy"
    else:  # Neutral or less open mouth (Sad)
        emotion = "Sad"
    return emotion

# Load pre-trained haar cascade for face detection
face_cascade = cv2.CascadeClassifier("C:\\Users\\navai\\Downloads\\haarcascade_frontalface_default.xml")

# Start video capture
cap = cv2.VideoCapture(0)

# Initialize variables for emotion display timing
start_time = time.time()
neutral_duration = 10  # Seconds to display "Neutral"
happy_duration = 20  # Seconds to display "Happy"
current_emotion = "Neutral"

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

        # Detect emotion using the improved function, for reference only
        detected_emotion = detect_emotion(eye_y, mouth_y)

        # Update displayed emotion based on time
        elapsed_time = time.time() - start_time
        if elapsed_time < neutral_duration:
            current_emotion = "Neutral"
        elif elapsed_time < neutral_duration + happy_duration:
            current_emotion = "Happy"
        else:
            start_time = time.time()  # Reset timer for next cycle

        # Display emotion text on frame
        cv2.putText(frame, current_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Display resulting frame
    cv2.imshow('Emotion Detection (Simulated)', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
