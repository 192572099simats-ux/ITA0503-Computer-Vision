import cv2
import numpy as np
image = cv2.imread("input.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = np.ones((9, 9), np.uint8)
top_hat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Original Image", gray)
cv2.imshow("Top Hat Image", top_hat)
cv2.imwrite("top_hat_output.jpg", top_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
