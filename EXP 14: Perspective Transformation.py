import cv2
import numpy as np
image = cv2.imread("image.jpg")
rows, cols = image.shape[:2]
pts1 = np.float32([[50,50],[300,50],[50,300],[300,300]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(image, matrix, (cols, rows))
cv2.imshow("Perspective", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
