import numpy as np
import cv2
import matplotlib.pyplot as plt

"""
在过滤(filtering)图片时, Border 类型对于保持图片大小起决定作用. 因为 filters 会扩展图片的
边界(edge). 
"""

img = cv2.imread('images/leaves.png')
red = [0, 0, 255]  # boarder color

# Border 类型
# cv2.BORDER_REPLICATE - Last element is replicated throughout for the total
# width specified, for example:  11111|1234567|777777 直接用边界的颜色填充
#
# cv2.BORDER_REFLECT - Border will be mirror reflection of the elements near
# the edges, for example : 54321|1234567|76543 倒映
#
# cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT - Similar to cv2.BORDER_REFLECT
# but, the value at the edge is not refelcted, for example: 65432|1234567|65432
# 倒映，和上面类似，但在倒映时，会把边界空开
#
# cv2.BORDER_WRAP - Pulls the border from the opposite edge. It will look like
# this : 34567|1234567|12345 上下, 左右重复.
#
# cv2.BORDER_CONSTANT - Adds a constant colored border. The value in RGB or BGR
# should be given as next argument. In this case Red [255, 0,0] 常量，增加的变量通
# 通为value色

border_w = [75, 75, 75, 75]
replicate = cv2.copyMakeBorder(img, *border_w, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, *border_w, cv2.BORDER_REFLECT)
reflect_101 = cv2.copyMakeBorder(img, *border_w, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, *border_w, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, *border_w, cv2.BORDER_CONSTANT, value=red)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
replicate_rgb = cv2.cvtColor(replicate, cv2.COLOR_BGR2RGB)
reflect_rgb = cv2.cvtColor(reflect, cv2.COLOR_BGR2RGB)
reflect_101_rgb = cv2.cvtColor(reflect_101, cv2.COLOR_BGR2RGB)
wrap_rgb = cv2.cvtColor(wrap, cv2.COLOR_BGR2RGB)
constant_rgb = cv2.cvtColor(constant, cv2.COLOR_BGR2RGB)

plt.subplot(231), plt.imshow(img_rgb), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(232), plt.imshow(replicate_rgb), plt.title('REPLICATE')
plt.xticks([]), plt.yticks([])

plt.subplot(233), plt.imshow(reflect_rgb), plt.title('REFLECT')
plt.xticks([]), plt.yticks([])

plt.subplot(234), plt.imshow(reflect_101_rgb), plt.title('REFLECT_101')
plt.xticks([]), plt.yticks([])

plt.subplot(235), plt.imshow(wrap_rgb), plt.title('WRAP')
plt.xticks([]), plt.yticks([])

plt.subplot(236), plt.imshow(constant_rgb), plt.title('CONSTANT')
plt.xticks([]), plt.yticks([])

plt.show()

# 结论: 通常采用 reflection 作为 boarder
# TODO: 通过数据说明为何 reflection 最好
