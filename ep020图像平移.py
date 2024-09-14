# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep020图像平移.py
    @时间：2024/2/26 17:19
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('lena_copy.jpg', flags=1)
rows, cols, ch = img.shape

# 平移变换矩阵：
dx, dy = 100, 50  # dx=100 向右偏移量, dy=50 向下偏移量
MAT = np.float32([[1, 0, dx], [0, 1, dy]])  # 构造平移变换矩阵

# dst = cv.warpAffine(img, MAT, (cols, rows))  # 默认为黑色填充
# dst = cv.warpAffine(img, MAT, (cols, rows), borderValue=(255, 255, 255))  # 设置白色填充
dst = cv.warpAffine(img, MAT, (cols, rows), flags=cv.INTER_LINEAR, borderValue=(255, 255, 255))

plt.figure(figsize=(9, 6))
plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title("Original")
plt.subplot(122), plt.imshow(cv.cvtColor(dst, cv.COLOR_BGR2RGB)), plt.title("Translational")
plt.show()

