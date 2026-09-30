import cv2

# ////////////Kernel different structures//////////////////////////////
kernel_MORPH_RECT = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
print("this is MORPH_RECT->", kernel_MORPH_RECT)

kernel_MORPH_ELLIPSE = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
print("this is MORPH_ELLIPSE->", kernel_MORPH_ELLIPSE)

kernel_MORPH_CROSS = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
print("this is MORPH_CROSS->", kernel_MORPH_CROSS)
