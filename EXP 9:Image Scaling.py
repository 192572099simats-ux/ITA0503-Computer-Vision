import cv2
image = cv2.imread("image.jpg")
small = cv2.resize(image, (300,200))
big = cv2.resize(image, (800,600))
cv2.imshow("Original", image)
cv2.imshow("Small", small)
cv2.imshow("Big", big)
cv2.waitKey(0)
cv2.destroyAllWindows()
