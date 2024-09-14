# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep005图像的通道.py
    @时间：2024/2/20 11:54
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np

img = cv.imread('lena_copy.jpg')

img_B = img[:, :, 0]
img_G = img[:, :, 1]
img_R = img[:, :, 2]

# BGR 通道拆分
bImg, gImg, rImg = cv.split(img)  # 拆分为 BGR 独立通道

# 将单通道扩展为三通道
imgZeros = np.zeros_like(img)  # 创建与 img1 相同形状的黑色图像
imgZeros[:, :, 2] = rImg  # 在黑色图像模板添加红色分量 rImg
cv.imshow("channel R", imgZeros)  # 扩展为 BGR 通道

cv.imshow('img_B', img_B)
cv.imshow('img_G', img_G)
cv.imshow('img_R', img_R)

cv.waitKey(0)
cv.destroyAllWindows()