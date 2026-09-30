import cv2

image = cv2.imread("image.jpeg")

# Convert the image to grayscale
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# #////// Apply a binary threshold to the grayscale image
# binary_img = cv2.threshold(gray_img, 100, 255, cv2.THRESH_BINARY)
# # print(binary_img)  # Print the threshold value used
# cv2.imshow("Binary Image", binary_img[1])
# # cv2.imshow("Grayscale Image", gray_img)
# # cv2.imshow("Original Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# /////apply an adaptive threshold to the grayscale image
# adaptive_img = cv2.adaptiveThreshold(
#     gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
# )
# cv2.imshow("Image", adaptive_img)
# cv2.imshow("Grayscale Image", gray_img)
# cv2.imshow("Original Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# /////apply an Otsu's threshold to the grayscale image
otsu_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("image", otsu_img[1])
cv2.imshow("Grayscale Image", gray_img)
cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
