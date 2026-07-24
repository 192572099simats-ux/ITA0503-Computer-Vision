import cv2
image = cv2.imread("image.jpg",0)
sobel = cv2.Sobel(image, cv2.CV_64F,1,1,ksize=5)
cv2.imshow("Sobel", sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
