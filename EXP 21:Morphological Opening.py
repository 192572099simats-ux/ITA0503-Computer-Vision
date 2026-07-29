import cv2
import numpy as np
image = cv2.imread("input.jpg")
if image is None:
    print("Error: Image not found!")
    exit()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary)
cv2.imshow("Opening Result", opening)
cv2.imwrite("opening_output.jpg", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
