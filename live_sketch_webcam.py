"""
How to make your webcam in to a pencil drawing video
First at all: we gonna need to install openCV via command: pip install opencv
"""

import cv2


def live_sketch(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_gray_blur = cv2.GaussianBlur(image_gray, (5, 5), 0)
    edges = cv2.Canny(image_gray_blur, 10, 30)
    img, thresh = cv2.threshold(edges, 55, 255, cv2.THRESH_BINARY_INV)
    return thresh


webcam_video_capture = cv2.VideoCapture(0)

while True:
    img, frame = webcam_video_capture.read()
    cv2.imshow('Pencil drawing webcam', live_sketch(frame))
    if cv2.waitKey(1) == 5:
        break

webcam_video_capture.release()
cv2.destroyAllWindows()
