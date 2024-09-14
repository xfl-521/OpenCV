# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep011图像加法.py
    @时间：2024/2/20 15:50
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('lena_copy.jpg', flags=1)
img2 = cv.imread('flowers.jpg', flags=1)

imgAddCV = cv.add(img1, img2)  # OpenCV 加法: 饱和运算，会导致图像变亮，数据溢出
imgAddNP = img1 + img2  # Numpy 加法: 模运算，会导致图像变暗

plt.subplot(221), plt.title("1. img1"), plt.axis('off')
plt.imshow(cv.cvtColor(img1, cv.COLOR_BGR2RGB))  # 显示 img1(RGB)
plt.subplot(222), plt.title("2. img2"), plt.axis('off')
plt.imshow(cv.cvtColor(img2, cv.COLOR_BGR2RGB))  # 显示 img2(RGB)
plt.subplot(223), plt.title("3. cv2.add(img1, img2)"), plt.axis('off')
plt.imshow(cv.cvtColor(imgAddCV, cv.COLOR_BGR2RGB))  # 显示 imgAddCV(RGB)
plt.subplot(224), plt.title("4. img1 + img2"), plt.axis('off')
plt.imshow(cv.cvtColor(imgAddNP, cv.COLOR_BGR2RGB))  # 显示 imgAddNP(RGB)
plt.show()

Value = 100  # 常数
Scalar = np.ones((1, 3), dtype="float") * Value  # 标量
imgAddV = cv.add(img1, Value)  # OpenCV 加法: 图像 + 常数，只在第二个蓝色通道上进行加法运算，图像会偏蓝
imgAddS = cv.add(img1, Scalar)  # OpenCV 加法: 图像 + 标量，在所有的通道上进行加法运算，图像变亮

plt.subplot(131), plt.title("1. img1"), plt.axis('off')
plt.imshow(cv.cvtColor(img1, cv.COLOR_BGR2RGB))  # 显示 img1(RGB)
plt.subplot(132), plt.title("2. img + constant"), plt.axis('off')
plt.imshow(cv.cvtColor(imgAddV, cv.COLOR_BGR2RGB))  # 显示 imgAddV(RGB)
plt.subplot(133), plt.title("3. img + scalar"), plt.axis('off')
plt.imshow(cv.cvtColor(imgAddS, cv.COLOR_BGR2RGB))  # 显示 imgAddS(RGB)
plt.show()

