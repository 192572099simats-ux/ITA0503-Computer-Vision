import cv2
image = cv2.imread("image.jpg")
rotate = cv2.rotate(image, cv2.ROTATE_180)
cv2.imshow("Original", image)
cv2.imshow("180 Degree", rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
