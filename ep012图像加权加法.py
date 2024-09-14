# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep012图像加权加法.py
    @时间：2024/2/21 10:37
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('lena_copy.jpg')
img2 = cv.imread('flowers.jpg')

img = cv.addWeighted(img1, 0.6, img2, 0.4, 0)
'''
    cv.addWeighted(scr1, alpha, scr2, beta, gamma[, dtype]) -> dst
    
    scr1, scr2：ndarray 多维数组，表示一个灰度或彩色图像
    alpha：第一张图像 scr1 的权重，通常取为 0～1 之间的浮点数
    beta：第二张图像 scr2 的权重，通常取为 0～1 之间的浮点数
    gamma： 灰度系数，图像校正的偏移量，用于调节亮度
    dtype 输出图像的深度，即每个像素值的位数，可选项，默认等于 src1.depth()
    返回值：dst，加权加法运算结果的图像数组
'''

imgAddW1 = cv.addWeighted(img1, 0.2, img2, 0.8, 0)  # 加权相加, a=0.2, b=0.8
imgAddW2 = cv.addWeighted(img1, 0.5, img2, 0.5, 0)  # 加权相加, a=0.5, b=0.5
imgAddW3 = cv.addWeighted(img1, 0.8, img2, 0.2, 0)  # 加权相加, a=0.8, b=0.2

plt.subplot(131), plt.title("1. a=0.2, b=0.8"), plt.axis('off')
plt.imshow(cv.cvtColor(imgAddW1, cv.COLOR_BGR2RGB))  # 显示 img1(RGB)
plt.subplot(132), plt.title("2. a=0.5, b=0.5"), plt.axis('off')
plt.imshow(cv.cvtColor(imgAddW2, cv.COLOR_BGR2RGB))  # 显示 imgAddV(RGB)
plt.subplot(133), plt.title("3. a=0.8, b=0.2"), plt.axis('off')
plt.imshow(cv.cvtColor(imgAddW3, cv.COLOR_BGR2RGB))  # 显示 imgAddS(RGB)
plt.show()

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()