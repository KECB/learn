import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('images/saturn.png', 0)
# cv2.imshow('Original Saturn Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


def add_gaussian_noise():
    im = np.zeros(img.shape[:2], np.uint8)
    mean = 0

    for i, sigma in enumerate(range(5, 51, 5)):
        gaussian = cv2.randn(im, mean, sigma)
        saturn_gauss = cv2.add(img, gaussian)
        plt.subplot(2, 5, i + 1), plt.imshow(saturn_gauss, cmap='gray')
        plt.title('Sigma = {}'.format(sigma))
        plt.xticks([]), plt.yticks([])
    plt.show()

    # noise 的影响
    plt.subplot(1, 3, 1)
    plt.plot(img[49, :])
    plt.subplot(1, 3, 2)
    plt.plot(gaussian[49, :])
    plt.subplot(1, 3, 3)
    plt.plot(saturn_gauss[49, :])
    plt.show()


def add_slat_pepper_noise():
    moon = cv2.imread('images/moon.png', 0)

    rows, cols = moon.shape
    salt_vs_pepper_ratio = 0.5  # 比例
    amount = 0.007  # 总数百分比
    moon_salted_and_peppered = moon.copy()
    num_salt = np.ceil(amount * moon.size * salt_vs_pepper_ratio)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in moon.shape]
    moon_salted_and_peppered[coords] = 255  # 白色
    num_pepper = np.ceil(amount * moon.size * (1 - salt_vs_pepper_ratio))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in moon.shape]
    moon_salted_and_peppered[coords] = 0  # 黑色

    cv2.imshow('Salt & peppered Moon', moon_salted_and_peppered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


add_gaussian_noise()
# add_slat_pepper_noise()
