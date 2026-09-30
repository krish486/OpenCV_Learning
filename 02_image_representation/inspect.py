import cv2

image = cv2.imread("image.jpeg")

print("shape of image:", image.shape)
print("size of image:", image.size)
print("first pixel value:", image[0, 0])


# //////////image breakdown/////////
pixel = image[0, 0]
blue = pixel[0]
green = pixel[1]
red = pixel[2]
print("blue value:", blue)
print("green value:", green)
print("red value:", red)

# /////////image modification/////////
# for i in range(image.shape[0]):
#     for j in range(image.shape[1]):
#         if (i + j) % 2 == 0:
#             image[i, j] = [0, 255, 0]  # green color

# cv2.imshow("Modified Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# /////////convert color image into grayscale/////////

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
