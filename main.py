import cv2

# Start webcam
cap = cv2.VideoCapture(0)

# Load Haar cascade from your folder
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

while True:
    # Read frames from the webcam
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    # Draw rectangle around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Show face count on the screen
    face_count_text = f'Faces Detected: {len(faces)}'
    cv2.putText(frame, face_count_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the result
    cv2.imshow('Face Detection', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
