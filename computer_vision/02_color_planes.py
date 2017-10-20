import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib import gridspec


# 读取图片并显示
img = cv2.imread('images/fruit.png')
cv2.imshow('Fruit Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 理解 Image Shape
# 彩色图片的 shape 一般由三个数字组成:  height(# of rows), width(# of columns) 和 color
# planes (BGR)
height, width, channels = img.shape
print('Image height: {}, Width: {}, # of channels: {}'.format(height, width,
                                                              channels))

# 显示不同颜色平面( plane)
# OpenCV读取的方式是 BGR, 因此 channel 0 是蓝色, 1是绿色, 2是红色
fruit_blues = img[:, :, 0]
fruit_greens = img[:, :, 1]
fruit_reds = img[:, :, 2]

# 显示不同颜色平面
cv2.imshow('Blue Fruit', fruit_blues)
cv2.imshow('Green Fruit', fruit_greens)
cv2.imshow('Red Fruit', fruit_reds)
cv2.waitKey(0) & 0xff
cv2.destroyAllWindows()

# 通过单行数据检验颜色平面数值
# plot values for each color plane on a specific row
fig = plt.figure(figsize=(10, 4))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1])

# original image
ax0 = plt.subplot(gs[0])
ax0.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax0.axhline(50, color='black')
ax0.axvline(100, color='k'), ax0.axvline(255, color='k')

# image slice
ax1 = plt.subplot(gs[1])
ax1.plot(fruit_blues[49, :], color='blue')
ax1.plot(fruit_greens[49, :], color='green')
ax1.plot(fruit_reds[49, :], color='red')
ax1.axvline(100, color='k', linewidth=2), ax1.axvline(255, color='k',
                                                      linewidth=2)

plt.suptitle('Examining Color Plane Values for a Single Row.')
plt.show()
