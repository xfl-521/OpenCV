# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep013图像不同尺寸加法.py
    @时间：2024/2/21 16:22
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np

imgS = cv.imread('lena_copy.jpg')
imgL = cv.imread('flower.jpg')

print(imgS.shape,
      imgL.shape)

x, y = 300, 50  # 叠放位置
W1, H1, C1 = imgL.shape
W2, H2, C2 = imgS.shape

if (x + W2) > W1:
    x = W1 - W2  # 调整图像叠放位置，避免溢出
if (y + H2) > H1:
    y = H1 - H2

imgCrop = imgL[y:y + H2, x:x + W2]  # 裁剪大图，与小图 imgS 的大小相同
imgAdd = cv.add(imgCrop, imgS)  # cv2 加法，裁剪图与小图叠加
alpha, beta, gamma = 0.2, 0.8, 0.0  # 加法权值
imgAddW = cv.addWeighted(imgCrop, alpha, imgS, beta, gamma)  # 加权加法，裁剪图与小图叠加

imgAddM = np.array(imgL)
imgAddM[y:y + H2, x:x + W2] = imgAddW  # 用叠加小图替换原图 imgL 的叠放位置

cv.imshow("imgAdd", imgAdd)
cv.imshow("imgAddW", imgAddW)
cv.imshow("imgAddM", imgAddM)
cv.waitKey(0)
