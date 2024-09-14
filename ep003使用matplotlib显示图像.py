# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep003使用matplotlib显示图像.py
    @时间：2024/2/20 11:02
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['FangSong']  # 支持中文标签

img = cv.imread('lena_copy.jpg', flags=1)  # flags=1 读取彩色图像(BGR)

imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

plt.subplot(221), plt.title("1. RGB 格式(mpl)"), plt.axis('off')
plt.imshow(imgRGB)  # matplotlib 显示彩色图像(RGB格式)，图像显示异常
plt.subplot(222), plt.title("2. BGR 格式(OpenCV)"), plt.axis('off')
plt.imshow(img)  # matplotlib 显示彩色图像(BGR格式)，图像显示异常
plt.subplot(223), plt.title("3. 设置 Gray 参数"), plt.axis('off')
plt.imshow(img2, cmap='gray')  # matplotlib 显示灰度图像，设置 Gray 参数
plt.subplot(224), plt.title("4. 未设置 Gray 参数"), plt.axis('off')
plt.imshow(img2)  # matplotlib 显示灰度图像，未设置 Gray 参数，图像显示异常

# plt.imshow(imgRGB)

plt.show()
#
# cv.imshow("img", img2)
# cv.waitKey(0)
# cv.destroyAllWindows()