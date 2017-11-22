import numpy as np
import cv2
import matplotlib.pyplot as plt
import scipy.stats as st


img = cv2.imread('images/saturn.png', 0)
# cv2.imshow('Original', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


def cv2_blue():
    # BLURRING WITH cv2.blur()
    # the first argument is the img, the second argument is the size of a normalized
    # box filter (w, h) below is an example of a 3 x 3 box filter
    #
    #            |  1  1  1 |
    #  k = 1/9 * | 1  1  1 |
    #            | 1  1  1 |
    #
    # using matplotlib to plot the two images (original/blur) side by side
    box_blur = cv2.blur(img, (5, 5))  # 5 x 5 盒子滤镜
    plt.subplot(121), plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(box_blur, cmap='gray', interpolation='bicubic')
    plt.title('Box Blur 5 x 5'), plt.xticks([]), plt.yticks([])
    plt.show()


# Creating and inspecting Gaussian Kernels Manually
def gaussian_kernel(k_size, sigma=5):
    """
    :param k_size : 必须为奇数
    :return: a 2D Gaussian Kernel array.
    """
    intervel = (2 * sigma + 1.) / k_size  # 间隔公式: (2 * sigma + 1) / kernel_size
    # TODO 用纯 numpy 处理
    x = np.linspace(-sigma - intervel/2., sigma + intervel/2., k_size + 1)
    k_1d = np.diff(st.norm.cdf(x))
    k_raw = np.sqrt(np.outer(k_1d, k_1d))
    k = k_raw / k_raw.sum()
    return k

gaussians = []
for sigma in range(1, 11):
    gaussians.append(gaussian_kernel(21, sigma))

for i, gauss in enumerate(gaussians):
    plt.subplot(2, 5, i + 1)  # subplot
    plt.imshow(gauss), plt.xticks([]), plt.yticks([])
    plt.title('Sigma = ' + str(i + 1), fontsize=9)
plt.show()

gaussian_blur = cv2.GaussianBlur(img, (11, 11), 1)
cv2.imshow('Gaussian Blur 11 x 11, Sigma = 1', gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2_blue()

