import cv2
image = cv2.imread("image.jpg")
cv2.putText(image,"WATERMARK",(50,50),
cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.imshow("Watermark", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
