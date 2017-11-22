import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

def sobel_filter(im, k_size):

    im = im.astype(np.float)
    width, height, c = im.shape
    if c > 1:
        img = 0.2126 * im[:, :, 0] + 0.7152 * im[:, :, 1] + 0.0722 * im[:, :, 2]
    else:
        img = im

    assert (k_size == 3 or k_size == 5);

    if k_size == 3:
        kh = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float)
        kv = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], dtype=np.float)
    else:
        kh = np.array([[-1, -2, 0, 2, 1],
                       [-4, -8, 0, 8, 4],
                       [-6, -12, 0, 12, 6],
                       [-4, -8, 0, 8, 4],
                       [-1, -2, 0, 2, 1]], dtype=np.float)
        kv = np.array([[1, 4, 6, 4, 1],
                       [2, 8, 12, 8, 2],
                       [0, 0, 0, 0, 0],
                       [-2, -8, -12, -8, -2],
                       [-1, -4, -6, -4, -1]], dtype=np.float)


    gx = convolve2d(img, kh, mode='same', boundary='symm', fillvalue=0)
    gy = convolve2d(img, kv, mode='same', boundary='symm', fillvalue=0)

    g = np.sqrt(gx * gx + gy * gy)
    g *= 255.0 / np.max(g)

    return g

# img = cv2.imread('images/android.png')
# im = sobel_filter(img, 5)
#
# plt.figure()
# plt.imshow(im, cmap=plt.cm.gray)
# plt.show()


