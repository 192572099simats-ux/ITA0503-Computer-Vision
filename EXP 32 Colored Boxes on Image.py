import cv2
import numpy as np
def create_image(width, height):
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    box_w = width // 10
    box_h = height // 10
    image[0:box_h, 0:box_w] = [0, 0, 0]
    image[0:box_h, width-box_w:width] = [255, 0, 0]
    image[height-box_h:height, 0:box_w] = [0, 255, 0]
    image[height-box_h:height, width-box_w:width] = [0, 0, 255]
    return image
width = int(input("Enter image width: "))
height = int(input("Enter image height: "))
result = create_image(width, height)
cv2.imshow("White Image with Colored Boxes", result)
cv2.imwrite("colored_boxes.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
