import os
import time
import cv2
import numpy as np
from PIL import Image
from threading import Thread

# -------------- image labesl ------------------------

def getImagesAndLabels(path):
    if not os.path.exists(path):
        os.makedirs(path)
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # print(imagePaths)

    # create empth face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        print("Loaded image:", imagePath, "Label:", Id)  # Add this line to debug
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids


# ----------- train images function ---------------
def TrainImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    harcascadePath = "C:/Users/Mohammed Faraz/Downloads/FRAS/FRAS/xml/haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("TrainingImage")
    """ Thread(target = recognizer.train, args=(faces, np.array(Id))).start()
    # Below line is optional for a visual counter effect
    Thread(target = counter_img("TrainingImage")).start()
    recognizer.save("TrainingImageLabel"+os.sep+"Trainner.yml")
    print("All Images") """
    try:
        recognizer.train(faces, np.array(Id))
        recognizer.save("FRAS/TrainingImageLabel"+os.sep+"Trainner.yml")
        print("Training completed.")
    except Exception as e:
        print("Error during training:", e)


# Optional, adds a counter for images trained (You can remove it)
""" def counter_img(path):
    imgcounter = 1
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    for imagePath in imagePaths:
        print(str(imgcounter) + " Images Trained", end="\r")
        time.sleep(0.008)
        imgcounter += 1 """

def counter_img(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    img_count = len(imagePaths)
    for i in range(1, img_count + 1):
        print(f"{i}/{img_count} Images Trained", end="\r")
        time.sleep(0.1)

# Main function
def main():
    # Start training
    t1 = Thread(target=TrainImages)
    t1.start()
    # Start counter
    t2 = Thread(target=counter_img, args=("TrainingImage",))
    t2.start()

    # Wait for both threads to finish
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()