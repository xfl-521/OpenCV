# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep027图像复合变换.py
    @时间：2024/2/27 17:51
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena_copy.jpg', flags=1)  # 读取彩色图像(BGR)
height, width = img.shape[:2]  # 图片的高度和宽度

# 缩放
fx, fy = 0.6, 0.6
MAZ = np.float32([[fx, 0, 0], [0, fy, 0]])  # 构造缩放变换矩阵
imgT1 = cv2.warpAffine(img, MAZ, (width, height), borderValue=(255, 255, 255))  # 仿射变换, 黑色填充
# 平移
dx, dy = 50, 200  # dx=100 向右偏移量, dy=50 向下偏移量
MAT = np.float32([[1, 0, dx], [0, 1, dy]])  # 构造平移变换矩阵
imgT2 = cv2.warpAffine(imgT1, MAT, (width, height), borderValue=(0, 0, 255))  # 实现仿射变换
# 旋转
theta = -30 * np.pi / 180  # 逆时针旋转 30°
cosTheta = np.cos(theta)
sinTheta = np.sin(theta)
MAR = np.float32([[cosTheta, -sinTheta, 0], [sinTheta, cosTheta, 0]])  # 构造旋转变换矩阵
imgT3 = cv2.warpAffine(imgT2, MAR, (width, height), borderValue=(0, 255, 0))  # 实现仿射变换
# 扭曲
theta = -30 * np.pi / 180  # 逆时针扭变 30°
MAS = np.float32([[1, np.tan(theta), 0], [0, 1, 0]])  # 构造扭变变换矩阵
imgT4 = cv2.warpAffine(imgT3, MAS, (width, height), borderValue=(255, 0, 0))  # 实现仿射变换

plt.figure(figsize=(9, 6))
plt.subplot(221), plt.axis('off'), plt.title("T1:Zoom")
plt.imshow(cv2.cvtColor(imgT1, cv2.COLOR_BGR2RGB)),
plt.subplot(222), plt.axis('off'), plt.title("T2:Translation")
plt.imshow(cv2.cvtColor(imgT2, cv2.COLOR_BGR2RGB))
plt.subplot(223), plt.axis('off'), plt.title("T3:Rotation")
plt.imshow(cv2.cvtColor(imgT3, cv2.COLOR_BGR2RGB))
plt.subplot(224), plt.axis('off'), plt.title("T4:Shear")
plt.imshow(cv2.cvtColor(imgT4, cv2.COLOR_BGR2RGB))
plt.show()
