import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('images/saturn.png', 0)

# 创建一个带噪声的图片
im = np.zeros(img.shape, np.uint8)
mean = 0
sigma_noise = 30
gaussian = cv2.randn(im, mean, sigma_noise)
img_noise = cv2.add(img, gaussian)

gauss_noise_remv = cv2.GaussianBlur(img_noise, (1, 21), 2)

plt.figure(figsize=(10, 8))
plt.subplot(131), plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(img_noise, cmap='gray', interpolation='bicubic')
plt.title('Noisy'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(gauss_noise_remv, cmap='gray', interpolation='bicubic')
plt.title('Gaussian Noise Removal'), plt.xticks([]), plt.yticks([])
plt.show()
