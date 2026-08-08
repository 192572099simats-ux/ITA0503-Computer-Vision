import cv2
import numpy as np
def subtract_foreground(image_path):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 50, 50])
    upper = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
   foreground = cv2.bitwise_and(image, image, mask=mask)
   cv2.imshow("Original", image)
    cv2.imshow("Foreground", foreground)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_path = input("Enter image path: ")
subtract_foreground(image_path)
