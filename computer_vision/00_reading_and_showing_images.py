import numpy as np
import cv2


print('读取图片: \n')
# 读取图片
# 注意: OpenCV 会将图片(灰度或彩色)以3个通道(Channel) 的形式读取进来
#      如果想读取单通道, 则需要在第二个参数设置为0(其它都不可以)
img = cv2.imread('images/dolphin.png')
img_single_channel = cv2.imread('images/dolphin.png', 0)

print('The shape of img without second arg is: {}'.format(img.shape))
print('The shape of img_single_channel is : {}'.format(
    img_single_channel.shape))


print('显示图片\ n')
# 通过 OpenCV 的 imshow() 显示图片
#   1st 参数 --> 窗口名
#   2nd 参数 --> 需要显示的 image
# 显示的图片不仅仅是一张, 但是需要不同的窗口名
cv2.imshow('OpenCV imshow()', img)

# OpenCV waitKey() 在调用imshow() 后一定要调用
# 参数单位是 milliseconds. 函数会在按下任意按钮后等待指定 ms 后执行.
cv2.waitKey(0)

# 关闭所有窗口
# 如果想关闭特定窗口, 使用 cv2.destroyWindow() 参数 --> 窗体名称
cv2.destroyAllWindows()


