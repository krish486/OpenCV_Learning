import cv2

image = cv2.imread("image.jpeg")
# aespect_ratio = image.shape[1] / image.shape[0]

# ///////Resize the image to a specific width and height
# if image is not None:
#     resized_image = cv2.resize(image, (int(aespect_ratio * 100), 100))
#     cv2.imshow("Resized Image", resized_image)
#     cv2.imshow("Original Image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("better luck next time")


# /////flip a image/////////
# if image is not None:
#     flipped_image = cv2.flip(image, -1)  # Flip horizontally
#     cv2.imshow("Flipped Image", flipped_image)
#     cv2.imshow("Original Image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("better luck next time")


# ////////////draw a link
# if image is not None:
#     start_point = (50, 50)
#     ending_point = (200, 200)
#     color = (0, 255, 0)
#     thickness = 5
#     image_with_line = cv2.line(image, start_point, ending_point, color, thickness)
#     cv2.imshow("Image with Line", image_with_line)
#     cv2.imshow("Original Image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# ////////draw a rectangle//////////
# if image is not None:
#     top_left = (50, 50)
#     bottom_right = (100, 100)
#     color = (204, 56, 65)
#     thickness = 5
#     image_with_rectangle = cv2.rectangle(
#         image, top_left, bottom_right, color, thickness
#     )
#     cv2.imshow("Image with Rectangle", image_with_rectangle)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()