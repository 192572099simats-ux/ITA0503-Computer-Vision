import cv2
import numpy as np
def create_rectangle(width, height):
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    start_point = (width // 4, height // 4)
    end_point = (3 * width // 4, 3 * height // 4)
    cv2.rectangle(image, start_point, end_point, (0, 0, 255), 3)
    return image
width = int(input("Enter image width: "))
height = int(input("Enter image height: "))
image = create_rectangle(width, height)
cv2.imshow("Rectangle", image)
cv2.imwrite("rectangle.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
