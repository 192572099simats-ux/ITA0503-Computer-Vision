import cv2
# Read the image
image = cv2.imread("image.jpg")
# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Gray-scale Image", gray_image)
    # Save the grayscale image
    cv2.imwrite("gray_image.jpg", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
