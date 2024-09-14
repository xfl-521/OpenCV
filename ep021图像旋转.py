# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep021图像旋转.py
    @时间：2024/2/26 17:37
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time

img = cv.imread('lena_copy.jpg', flags=1)
rows, cols, ch = img.shape

# 确定旋转角度
angle = 10
theta = np.pi * (angle / 180.0)

# 绕着原点进行旋转
cosTheta = np.cos(theta)
sinTheta = np.sin(theta)
MAT = np.float32([[cosTheta, -sinTheta, 0], [sinTheta, cosTheta, 0]])  # 构造旋转变换矩阵
# dst = cv2.warpAffine(img, MAT, (cols, rows))  # 默认为黑色填充
dst = cv.warpAffine(img, MAT, (cols, rows), borderValue=(255, 255, 255))  # 设置白色填充

plt.figure(figsize=(9, 6))
plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title("Origin")
plt.subplot(122), plt.imshow(cv.cvtColor(dst, cv.COLOR_BGR2RGB)), plt.title("Rotation")
plt.show()

# 绕着中心点进行旋转（也可以是任意点）
height, width = img.shape[:2]  # 图片的高度和宽度
theta1 = 30  # 顺时针旋转角度，单位为角度
x0, y0 = width // 2, height // 2  # 以图像中心作为旋转中心
MAR1 = cv.getRotationMatrix2D((x0, y0), theta1, 1.0)
imgR1 = cv.warpAffine(img, MAR1, (width, height), borderValue=(255, 255, 255), borderMode=cv.BORDER_REFLECT)  # 旋转变换，默认为黑色填充

plt.figure(figsize=(10, 6))
plt.subplot(121), plt.axis('off'), plt.title(r"$Origin$")
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.subplot(122), plt.axis('off'), plt.title(r"$Rotation {}^o$".format(theta1))
plt.imshow(cv.cvtColor(imgR1, cv.COLOR_BGR2RGB))
plt.show()

# 特殊情况，旋转角度为直角，当旋转角度为 90，180，270 度时，可以用图像旋转函数 cv2.rotate(src, rotateCode)
imgR90 = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
imgR180 = cv.rotate(img, cv.ROTATE_180)
imgR270 = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)

# imgR90 = np.rot90(img, 1)  # numpy 矩阵旋转 90*1=90 度
# imgR180 = np.rot90(img, 2)  # numpy 矩阵旋转 90*2=180 度
# imgR270 = np.rot90(img, 3)  # numpy 矩阵旋转 90*3=270 度

plt.figure(figsize=(9, 7))
plt.subplot(221), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title(r"$Origin$")
plt.subplot(222), plt.imshow(cv.cvtColor(imgR90, cv.COLOR_BGR2RGB)), plt.title(r"$Rotation 90^{o}$")
plt.subplot(223), plt.imshow(cv.cvtColor(imgR180, cv.COLOR_BGR2RGB)), plt.title(r"$Rotation 180^{o}$")
plt.subplot(224), plt.imshow(cv.cvtColor(imgR270, cv.COLOR_BGR2RGB)), plt.title(r"$Rotation 270^{o}$")
plt.show()
