# Converting color images to shades of gray

# import openCV, but first install via: pip install opencv-python
import cv2

image = cv2.imread('./path/picture_name.jpg', 0)

cv2.imwrite('./path/new_black_and_white_picture_name.jpg', image)

cv2.imshow('Grayscale', image)

cv2.waitKey()
cv2.destroyAllWindows()
