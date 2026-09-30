import cv2

image = cv2.imread("image.jpeg")

# Convert the image to grayscale
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# /////////////Solel X//////////////////////////////
# # ////apply sobel edge detection to the grayscale image
# sobelX = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=5)
# # sobelX = cv2.convertScaleAbs(sobelX)
# cv2.imshow("Sobel X", sobelX)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ////////////Sobel Y//////////////////////////////
# # ////apply sobel edge detection to the grayscale image
# sobelY = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)
# cv2.imshow("Sobel Y", sobelY)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


