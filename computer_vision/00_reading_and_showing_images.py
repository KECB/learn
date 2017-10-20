import numpy as np
import matplotlib.pyplot as plt
import cv2


def read_img():
    """
    如何使用 OpenCV 读取图片
    :return:
    """
    # 读取图片
    # 注意: OpenCV 会将图片(灰度或彩色)以3个通道(Channel) 的形式读取进来
    #      如果想读取单通道, 则需要在第二个参数设置为0(其它都不可以)
    img = cv2.imread('images/dolphin.png')
    img_single_channel = cv2.imread('images/dolphin.png', 0)

    print('The shape of img without second arg is: {}'.format(img.shape))
    print('The shape of img_single_channel is : {}'.format(
        img_single_channel.shape))


def show_img():
    """
    如何使用 OpenCV 显示图片
    """
    img = cv2.imread('images/dolphin.png')
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

    # namedWindow()可以通过 flag 设置 window 的类型
    cv2.namedWindow('Named Resizable Window', cv2.WINDOW_NORMAL)
    cv2.imshow('Named Resizable Window', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def write_img():
    """
    如何使用 OpenCV 保存图片
    """
    img = cv2.imread('images/dolphin.png')
    # 使用 imwrite 写图片
    # 1st 参数 --> 目标文件名称
    # 2nd 参数 --> 想要保存的图片对象
    cv2.imwrite('images/dolphin2.png', img)

    # 通过 s 键保存
    img = cv2.imread('images/dolphin.png')
    cv2.imshow('Save image', img)
    print('按 "s" 键保存图片到 dolphin3.png')
    key = cv2.waitKey(0) & 0xff  # 64为需要增加0xff
    if key == 27:  # 如果是 ESC 键就退出
        cv2.destroyAllWindows()
    elif key == ord('s'):
        cv2.imwrite('images/dolphin3.png', img)
        cv2.destroyAllWindows()


def show_img_with_plt():
    """
    使用 matlibplot 显示图片.
    问题: 如何一个页面同时显示多张图片
    """
    # 单色图片显示
    img = cv2.imread('images/dolphin.png')
    plt.title('Monochromatic Images in Matplotlib')
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])
    plt.show()

    height, width = img.shape[:2]
    print('图片宽: {}px, 高: {}px'.format(width, height))
    print('图片类型: {}'.format(type(img)))

    # 彩色图片显示
    # 注意:  OpenCV 读取的图片是 BGR 模式. 但 Matplotlib 显示是使用 RGB 模式.
    #       所以直接显示会出现问题
    img_color = cv2.imread('images/fruit.png')
    plt.title('How OpenCV images (BGR) display in Matplotlib (RGB')
    plt.imshow(img_color)
    plt.xticks([]), plt.yticks([])
    plt.show()

    # 正确的显示方式
    img_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
    plt.title('Correct Display after converting with cv2.BGR2RGB')
    plt.imshow(img_rgb)
    plt.xticks([]), plt.yticks([])
    plt.show()


show_img_with_plt()
