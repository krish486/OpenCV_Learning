import cv2

img = cv2.imread("image.jpeg")

if img is None:
    print("Error: Could not read the image.")
else:
    cv2.imshow("mera img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#######################################

###save the image
# if img is not None:
#     cv2.imwrite("saveKiya.png", img)
# else:
#     print("Error: Could not read the image.")
