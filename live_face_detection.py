"""
Life face detection using webcam
Need to install openCV via command: pip install opencv-python
"""
import cv2
import time

# download haarcascade from: https://github.com/opencv/opencv/tree/master/data/haarcascades
face_classifier = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')


def face_detector(frame):
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.3, 5)

    if faces is ():
        return frame
    else:
        time.sleep(.1)

    for (x, y, width, height) in faces:
        rect = cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 255), 2)
        return rect


web_cam = cv2.VideoCapture(0)


while True:
    ret, frame = web_cam.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow('Face detector', face_detector(frame))
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

web_cam.release()
cv2.destroyAllWindows()
