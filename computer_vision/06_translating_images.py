import numpy as np
import cv2


# Translation is the shifting of objects location. If you know the shift in
# (x,y) direction, let it be (t_x,t_y), you can create the transformation matrix
# M as follows:
#
#      M =  | 1  0  t_x |
#           | 0  1  t_y |
#
# You'll need to make it into a Numpy array of type np.float32 and pass it into
# cv2.warpAffine() function.

img = cv2.imread('images/saturn.png', 0)
rows, cols = img.shape
translate_x = -150
translate_y = 50
M = np.float32([[1, 0, translate_x], [0, 1, translate_y]])

img_translated = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('Translated Image', img_translated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# WARNING: Third argument of the cv2.warpAffine() function is the size of the
# output image, which should be in the form of (width, height).
# Remember width = number of columns, and height = number of rows.
