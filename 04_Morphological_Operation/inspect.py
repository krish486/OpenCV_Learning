import cv2
import numpy as np

# ////////////Kernel different structures//////////////////////////////
# kernel_MORPH_RECT = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# print("this is MORPH_RECT->", kernel_MORPH_RECT)

# kernel_MORPH_ELLIPSE = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
# print("this is MORPH_ELLIPSE->", kernel_MORPH_ELLIPSE)

# kernel_MORPH_CROSS = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
# print("this is MORPH_CROSS->", kernel_MORPH_CROSS)

# //////////////////////////////////////
# create black image
img = np.zeros((300, 500), dtype=np.uint8)
cv2.rectangle(img, (50, 50), (250, 200), 255, -1)

# //add small noise to the image
cv2.circle(img, (300, 200), 5, 255, -1)
cv2.circle(img, (420, 240), 5, 255, -1)

# //add small noise inside the obeject
cv2.circle(img, (150, 100), 5, 0, -1)


# //create a 3X3 kernel with all ones
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))


# //Errosion
eroded = cv2.erode(img, kernel, iterations=1)
cv2.imshow("original", img)
cv2.imshow("eroded", eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
