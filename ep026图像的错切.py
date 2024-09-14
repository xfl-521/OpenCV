# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep026图像的错切.py
    @时间：2024/2/27 17:29
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 图像的错切变换也称斜切，是指平面景物在投影平面上的非垂直投影，使图像中的图形在水平方向或垂直方向产生扭变。
# 以水平扭变为例，像素点 (x,y) 在水平方向发生扭变变成斜边，而在垂直方向的边不变
img = cv.imread('lena_copy.jpg')
height, width = img.shape[:2]

# 图像扭变角度
x, y = 0.1, 0.1
MAS = np.float32([[1, x, 0], [y, 1, 0]])
imgShear = cv.warpAffine(img, MAS, (width, height), borderMode=cv.BORDER_REPLICATE)

plt.figure(figsize=(9, 6))
plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title("Origin")
plt.subplot(122), plt.imshow(cv.cvtColor(imgShear, cv.COLOR_BGR2RGB)), plt.title("Shear")
plt.show()
