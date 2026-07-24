import cv2
import numpy as np
image = cv2.imread("image.jpg")
kernel = np.ones((5,5), np.uint8)
dilate = cv2.dilate(image, kernel, iterations=1)
cv2.imshow("Original", image)
cv2.imshow("Dilated", dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()
