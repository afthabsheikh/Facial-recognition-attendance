# Facial-recognition-attendance
**Project Overview**

This project is a Facial Recognition Attendance System developed using Python and OpenCV (cv2). It is capable of recognizing faces in real-time and marking attendance automatically. The system also includes an automated email notification feature that sends alerts based on specific triggers, such as attendance marking or system usage.


**Features**

Real-Time Facial Recognition: Leverages OpenCV to detect and recognize faces using a webcam or pre-recorded video.
Attendance Management: Automatically logs attendance for recognized individuals.

Automated Email Notifications: Sends automated emails (e.g., attendance reports or alerts) using Python's SMTP library.

Face Training and Recognition: Train the system with new faces and recognize them in future sessions.

Easy-to-Use Interface: Simple command-line interface for interacting with the system.


**Technologies Used**

*Python 3.x

*OpenCV (cv2)

*SMTP (for email automation)

*Haar Cascade Classifier (for face detection)

*CSV (for managing attendance records)


**Installation**

Python 3.x

OpenCV Library (cv2)

smtplib for sending emails

numpy for numerical operations


**Steps**

Clone the repository:

git clone https://github.com/afthabsheikh/Facial-recognition-attendance.git

cd Facial-recognition-attendance

Install the required Python libraries: Run the following command to install dependencies from the requirements.txt file:

pip install -r requirements.txt

Prepare your dataset: Add images of individuals in the designated folder (TrainingImage) to be recognized by the system.

Train the recognizer: Use the Train_Image.py script to train the system with images from the dataset:

python FRAS/Train_Image.py


**How to Use**

1. Capture Images
Run the following script to capture images for facial recognition:

python FRAS/Capture_Image.py

2. Train the Model
After capturing images, train the model:

python FRAS/Train_Image.py

3. Recognize Faces and Mark Attendance
Once training is complete, use this script to start the recognition process and mark attendance:

python FRAS/Recognize.py

4. Check Attendance
Attendance records will be stored in a CSV file located in StudentDetails/StudentDetails.csv. You can view or download this file to review attendance.


**System Structure**

Capture_Image.py: Used to capture facial images from the webcam for training purposes.

Train_Image.py: Trains the recognizer using the captured images.

Recognize.py: Detects and recognizes faces in real-time and marks attendance.

automail.py / automail1.py: Scripts responsible for sending automated emails.

check_camera.py: Utility script to check if the camera is working properly.

TrainingImage/: Directory for storing training images of individuals.

TrainingImageLabel/: Stores the trained model files.

xml/: Contains the haarcascade_frontalface_default.xml file for facial detection.

**Automated Email Feature**

The system uses Python's smtplib to send email notifications automatically. You can configure the email settings in the automail.py script, including the SMTP server, email address, and password for sending emails.
