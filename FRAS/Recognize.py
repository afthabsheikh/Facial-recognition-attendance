import datetime
import os
import time
import cv2
import pandas as pd

# Configuration constants
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
SCALE_FACTOR = 1.2
MIN_NEIGHBORS = 5
MIN_CONFIDENCE = 40
SUCCESS_THRESHOLD = 40

def recognize_attendance():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(os.path.join("C:/Users/Mohammed Faraz/Downloads/FRAS/FRAS/TrainingImageLabel/Trainner.yml"))
    
    harcascade_path = os.path.join("C:/Users/Mohammed Faraz/Downloads/FRAS/FRAS/xml/haarcascade_frontalface_default.xml")
    face_cascade = cv2.CascadeClassifier(harcascade_path)
    
    df = pd.read_csv(os.path.join("C:/Users/Mohammed Faraz/Downloads/FRAS/StudentDetails", "StudentDetails.csv"))
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, CAMERA_WIDTH)  # set video width
    cam.set(4, CAMERA_HEIGHT)  # set video height
    min_w = 0.1 * cam.get(3)
    min_h = 0.1 * cam.get(4)

    total_attempts = 0
    successful_attempts = 0

    while True:
        ret, im = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=SCALE_FACTOR, minNeighbors=MIN_NEIGHBORS, minSize=(int(min_w), int(min_h)), flags=cv2.CASCADE_SCALE_IMAGE)

        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x+w, y+h), (10, 159, 255), 2)
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])

            name = 'Unknown'
            label = 'Unknown'
            conf_str = f"  {round(100 - conf)}%"

            if MIN_CONFIDENCE < conf < 100:
                name_query = df.loc[df['Id'] == Id]['Name'].values
                if name_query.size > 0:
                    name = name_query[0]
                conf_str = f"  {round(100 - conf)}%"
                label = f"{Id}-{name}"
                successful_attempts +=1
            else:
                conf_str = f"  {round(100 - conf)}%"
                label = 'Unknown'
            
            total_attempts +=1

            if 100 - conf > MIN_CONFIDENCE:
                timestamp = time.time()
                date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
                time_str = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
                attendance.loc[len(attendance)] = [Id, name, date, time_str]

            label = label if 100 - conf > MIN_CONFIDENCE else 'Unknown'
            status = "[Pass]" if 100 - conf > MIN_CONFIDENCE else ""
            cv2.putText(im, label + " " + status, (x+5, y-5), font, 1, (255, 255, 255), 2)

            color = (0, 255, 0) if 100 - conf > MIN_CONFIDENCE else (0, 255, 255) if 100 - conf > 30 else (0, 0, 255)
            cv2.putText(im, conf_str, (x + 5, y + h - 5), font, 1, color, 1)

        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('Attendance', im)

        if cv2.waitKey(1) == ord('q'):
            break

    # Save attendance log
    timestamp = time.time()
    date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    time_str = datetime.datetime.fromtimestamp(timestamp).strftime('%H-%M-%S')
    filename = os.path.join("Attendance", f"Attendance_{date}_{time_str}.csv")
    attendance.to_csv(filename, index=False)

    cam.release()
    cv2.destroyAllWindows()

    if total_attempts > 0:
        success_rate = (successful_attempts / total_attempts) * 100
        if success_rate > SUCCESS_THRESHOLD:
            print("Attendance is successful")
        else:
            print("Attendance is not successful")
    else:
        print("No faces detected")