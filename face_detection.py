# Face detection

# first install openCV via command: pip install opencv
import cv2

# download haarcascade_frontalface_default.xml
# from https://github.com/opencv/opencv/tree/master/data/haarcascades
face_classifier = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

image = cv2.imread('path_of_image')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces_detect = face_classifier.detectMultiScale(gray_image, 1.2, 5)

if faces_detect is ():
    print("No faces found.")

for (x, y, width, height) in faces_detect:
    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 255), 2)
    cv2.imshow('Face detection', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
