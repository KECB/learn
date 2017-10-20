import numpy as np
import cv2


img = cv2.imread('images/bicycle.png')
cv2.imshow('Bicycle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cropped = img[109:310, 9:160]
cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

