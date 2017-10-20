import numpy as np
import time
import cv2


bicycle = cv2.imread('images/bicycle.png', 0)
dolphin = cv2.imread('images/dolphin.png', 0)
coins = cv2.imread('images/coins.png', 0)

# cv2.imshow('Bicyle Image', bicycle)
# cv2.imshow('Dolphin Image', dolphin)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


def diff_between_numpy_cv():
    """
    在大于255后(8bit int), OpenCV addition 是饱和度计算, Numpy 是模计算
    """
    x = np.uint8([250])
    y = np.uint8([10])
    print('Open CV Addition: {}'.format(cv2.add(x, y)))  # 250+10 = 260 => 255
    print('Numpy Addition: {}'.format(x + y))  # 250+10 = 260 % 256 = 4


def add_images(img_1, img_2):
    """
    Open CV 相加如果两张图片大小相同则会使用 pairwise
    如果第二个参数使一个 scalar 则会使用 element-wise 相加
    """
    if img_1.shape == img_2.shape:
        sum_img = cv2.add(img_1, img_2)
        cv2.imshow('Summed Image', sum_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        scaled_img = cv2.add(img_1, 50)
        cv2.imshow('Scalar Addition on Bicycle Image', scaled_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print('Original Image [0: 5]: {}'.format(img_1[:5]))
        print('Scalar Image [0:5]: {}'.format(scaled_img[:5]))


def substract_images(img_1, img_2):
    """
    """
    # TODO: 研究下 substract 和 absdiff 区别
    if img_1.shape == img_2.shape:
        diff = cv2.absdiff(img_1, img_2)
        cv2.imshow('Abs Diff Image', diff)
        sub_1 = cv2.subtract(img_1, img_2)
        cv2.imshow('Substract 1 - 2', sub_1)
        sub_2 = cv2.subtract(img_2, img_1)
        cv2.imshow('Substract 2 - 1', sub_2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def averaging_images(img_1, img_2):
    """

    """
    if img_1.shape == img_2.shape:
        average_image = img_1 / 2 + img_2 / 2
        alt_average_img = cv2.add(img_1, img_2) / 2
        cv2.imshow('Averaged Image', average_image.astype('uint8'))
        cv2.imshow('Alt. Averaged Image', alt_average_img.astype('uint8'))
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def blend_images(img_1, img_2):
    """
    Alpha blending via the blending function cv2.addWeighted
    公式: g(x) = (1 - alpha)f_0(x) + alphaf_1(x)

    通过变换 Alpha 值, 区间[0, 1], 可以在两个图片间切换.
    注意:  alpha + beta = 1
          alpha => [0, 1]
          beta  => [0, 1]
    公式:  dst = alpha * img1 + beta * img2 + gamma
    gamma 相当于 Add 里的 scalar. 会增加亮度.
    """
    window_name = 'Alpha Blending Image'
    cv2.namedWindow(window_name)
    for alpha in range(0, 10, 1):
        alpha_blending = cv2.addWeighted(img_1, alpha / 10., dolphin,
                                         (10 - alpha) / 10., 0)
        cv2.imshow(window_name, alpha_blending)
        key = cv2.waitKey(0) & 0xff
        if key == 27:
            cv2.destroyAllWindows()
            break


    cv2.destroyAllWindows()


blend_images(bicycle, dolphin)
