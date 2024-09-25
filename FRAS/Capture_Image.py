import csv
import cv2
import os

# Function to check if a string is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

# Function to capture images
def takeImages():
    Id = input("Enter Your Id: ")
    name = input("Enter Your Name: ")

    if is_number(Id) and name.isalpha():
        cam = cv2.VideoCapture(0)
        harcascadePath = "C:/Users/Mohammed Faraz/Downloads/FRAS/FRAS/xml/haarcascade_frontalface_default.xml"
        
        # Check if the cascade file exists
        if not os.path.exists(harcascadePath):
            print(f"Error: The file {harcascadePath} does not exist.")
            return

        detector = cv2.CascadeClassifier(harcascadePath)
        
        # Check if the cascade file is loaded correctly
        if detector.empty():
            print("Error loading cascade file. Check the path and file name.")
            return

        sampleNum = 0
        if not os.path.exists("TrainingImage"):
            os.makedirs("TrainingImage")

        while True:
            ret, img = cam.read()
            if not ret:
                print("Failed to capture image from camera.")
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30,30))
            
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                sampleNum += 1
                cv2.imwrite(f"TrainingImage/{name}.{Id}.{sampleNum}.jpg", gray[y:y+h, x:x+w])
                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum >= 100:  # Changed to >= to capture exactly 100 images
                break

        cam.release()
        cv2.destroyAllWindows()
        
        # Save data to CSV
        res = f"Images Saved for ID : {Id} Name : {name}"
        header = ["Id", "Name"]
        row = [Id, name]

        if not os.path.exists("StudentDetails"):
            os.makedirs("StudentDetails")
        
        csv_file_path = "StudentDetails/StudentDetails.csv"
        file_exists = os.path.isfile(csv_file_path)
        
        with open(csv_file_path, 'a+', newline='') as csvFile:
            writer = csv.writer(csvFile)
            if not file_exists:
                writer.writerow(header)
            writer.writerow(row)
        
        print(res)
    else:
        if not is_number(Id):
            print("Enter Numeric ID")
        if not name.isalpha():
            print("Enter Alphabetical Name")

if __name__ == "__main__":
    takeImages()
