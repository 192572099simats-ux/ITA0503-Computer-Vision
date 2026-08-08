import cv2
import numpy as np
def subtract_background(image_path):
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([35, 40, 40])
    upper = np.array([85, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("Original", image)
    cv2.imshow("Background Subtracted", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_path = input("Enter image path: ")
subtract_background(image_path)
