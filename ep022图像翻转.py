# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep022图像翻转.py
    @时间：2024/2/26 18:29
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('lena_copy.jpg', flags=1)

imgFlip1 = cv.flip(img, 0)  # 垂直翻转
imgFlip2 = cv.flip(img, 1)  # 水平翻转
imgFlip3 = cv.flip(img, -1)  # 水平和垂直翻转

plt.figure(figsize=(9, 6))
plt.subplot(221), plt.axis('off'), plt.title("Original")
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))  # 原始图像
plt.subplot(222), plt.axis('off'), plt.title("Flipped Horizontally")
plt.imshow(cv.cvtColor(imgFlip2, cv.COLOR_BGR2RGB))  # 水平翻转
plt.subplot(223), plt.axis('off'), plt.title("Flipped Vertically")
plt.imshow(cv.cvtColor(imgFlip1, cv.COLOR_BGR2RGB))  # 垂直翻转
plt.subplot(224), plt.axis('off'), plt.title("Flipped Horizontally & Vertically")
plt.imshow(cv.cvtColor(imgFlip3, cv.COLOR_BGR2RGB))  # 水平垂直翻转
plt.show()
