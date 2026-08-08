import cv2
def add_text(image_path, text):
    image = cv2.imread(image_path)
    cv2.putText(image, text, (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)
    cv2.imshow("Text on Image", image)
    cv2.imwrite("text_image.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_path = input("Enter image path: ")
text = input("Enter text: ")
add_text(image_path, text)
