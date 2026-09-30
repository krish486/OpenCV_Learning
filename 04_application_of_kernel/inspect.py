import cv2

image = cv2.imread("image.jpeg")

# //////////Average Blurring//////////
# if image is None:
#     print("Error: Could not read image file")
# else:
#     blurred = cv2.blur(image, (10, 1))
#     cv2.imshow("Original Image", image)
#     cv2.imshow("Blurred Image", blurred)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# //////////Gaussian Blurring//////////
# if image is None:
#     print("Error: Could not read image file")
# else:
#     blurred = cv2.GaussianBlur(image, (5, 5), 10)
#     cv2.imshow("Original Image", image)
#     cv2.imshow("Blurred Image", blurred)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# //////////bilateral filtering//////////
# if image is None:
#     print("Error: Could not read image file")
# else:
#     blurred = cv2.bilateralFilter(image, 9, 75, 75)
#     cv2.imshow("Original Image", image)
#     cv2.imshow("Blurred Image", blurred)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
