# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep019图像的仿射变换.py
    @时间：2024/2/21 18:28
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 仿射变换：图像中的平行关系、面积比、共线线段或平行线段的长度比、矢量的线性组合不变
# 仿射变换是旋转和非均匀缩放的复合，典型的仿射变换是斜切。

img = cv.imread('lena_copy.jpg')  # 读取彩色图像(BGR)
rows, cols, ch = img.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])  # 初始位置
pts2 = np.float32([[50, 100], [200, 50], [100, 250]])  # 终止位置
MA = cv.getAffineTransform(pts1, pts2)  # 计算 2x3 变换矩阵 MA
dst = cv.warpAffine(img, MA, (cols, rows))  # 实现仿射变换

plt.figure(figsize=(9, 6))
plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title("Original")
plt.subplot(122), plt.imshow(cv.cvtColor(dst, cv.COLOR_BGR2RGB)), plt.title("warpAffine")
plt.show()
