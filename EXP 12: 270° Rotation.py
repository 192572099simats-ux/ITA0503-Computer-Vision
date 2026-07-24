import cv2
image = cv2.imread("image.jpg")
rotate = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Original", image)
cv2.imshow("270 Degree", rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
