import cv2
image = cv2.imread("image.jpg")
crop = image[100:300,100:300]
image[0:200,0:200] = crop
cv2.imshow("ROI", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
