import numpy as np
import cv2
import matplotlib.pyplot as plt


# bicycle_img = cv2.imread('images/bicycle.png', 0)
#
# sobelx = cv2.Sobel(bicycle_img, cv2.CV_64F, 1, 0, ksize=5)
# sobely = cv2.Sobel(bicycle_img, cv2.CV_64F, 0, 1, ksize=5)
#
#
# scharrx = cv2.Scharr(bicycle_img, cv2.CV_64F, 1, 0)
# scharry = cv2.Scharr(bicycle_img, cv2.CV_64F, 0, 1)
#
#
#
# # apply the laplacian filter to the image using OpenCV
# laplacian = cv2.Laplacian(bicycle_img, cv2.CV_64F)
#
# # show the original, sobel, scharr and
# plt.figure(figsize=(12, 8))
# plt.subplot(231),plt.imshow(bicycle_img, cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(232),plt.imshow(sobelx, cmap = 'gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(233),plt.imshow(sobely, cmap = 'gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
#
# # scharr
# plt.subplot(234),plt.imshow(scharrx, cmap = 'gray')
# plt.title('Scharr X'), plt.xticks([]), plt.yticks([])
# plt.subplot(235),plt.imshow(scharry, cmap = 'gray')
# plt.title('Scharr Y'), plt.xticks([]), plt.yticks([])
#
# # laplacian
# plt.subplot(236),plt.imshow(laplacian, cmap = 'gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
#
# plt.suptitle('Sobel, Scharr & Laplacian Edge Detection', fontsize=16)
# plt.tight_layout()
# plt.show()


img = cv2.imread('images/android.png', 0 )


sobelx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=5)

sobel_combine = sobelx + sobely

plt.subplot(131), plt.imshow(sobelx, cmap='gray')
plt.subplot(132), plt.imshow(sobely, cmap='gray')
plt.subplot(133), plt.imshow(sobel_combine, cmap='gray')
plt.show()
