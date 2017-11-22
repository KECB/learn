import numpy as np
import cv2
import matplotlib.pyplot as plt


saturn = cv2.imread('images/saturn.png', 0)

saturn_median = cv2.medianBlur(saturn, 21)

plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.imshow(saturn, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2)
plt.imshow(saturn_median, cmap='gray')
plt.title('Median Blur'), plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()