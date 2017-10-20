import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('images/dolphin.png', 0)
cv2.imshow("Dolphin Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('The intensity value at row 50 & column 100 is : {}'.format(img[49, 99]))

print('Row 50 column values:')
print(img[49, :])

print('Rows 101-103 & columns 201-203')
print(img[100:103, 200:203])

plt.plot(img[49, :])
plt.show()
