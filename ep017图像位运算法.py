# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep017图像位运算法.py
    @时间：2024/2/21 17:32
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1.29 图像的位操作
img1 = cv2.imread('lena_copy.jpg', flags=1)
img2 = cv2.imread('flowers.jpg', flags=1)

imgAnd = cv2.bitwise_and(img1, img2)
imgOr = cv2.bitwise_or(img1, img2)
imgNot = cv2.bitwise_not(img1)
imgXor = cv2.bitwise_xor(img1, img2)

plt.figure(figsize=(9, 6))
titleList = ["img1", "img2", "and", "or", "not", "xor"]
imageList = [img1, img2, imgAnd, imgOr, imgNot, imgXor]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.title(titleList[i]), plt.axis('off')
    plt.imshow(cv2.cvtColor(imageList[i], cv2.COLOR_BGR2RGB), 'gray')
plt.show()

