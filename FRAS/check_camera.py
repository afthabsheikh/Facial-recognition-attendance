import cv2
import os

def camer():
    # Load the cascade
    harcascadePath = 'C:/Users/Mohammed Faraz/Downloads/FRAS/FRAS/xml/haarcascade_frontalface_default.xml'
    
    # Check if the cascade file exists
    if not os.path.exists(harcascadePath):
        print(f"Error: The file {harcascadePath} does not exist.")
        return
    
    face_cascade = cv2.CascadeClassifier(harcascadePath)
    
    # Check if the cascade file is loaded correctly
    if face_cascade.empty():
        print("Error loading cascade file. Check the path and file name.")
        return

    # To capture video from webcam.
    cap = cv2.VideoCapture(0)

    while True:
        # Read the frame
        ret, img = cap.read()
        if not ret:
            print("Failed to capture image from camera.")
            break

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (10, 159, 255), 2)

        # Display
        cv2.imshow('Webcam Check', img)

        # Stop if escape or 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()
