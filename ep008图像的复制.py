# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep008图像的复制.py
    @时间：2024/2/20 12:29
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np

img = cv.imread('lena_copy.jpg', flags=1)

img1 = img
img2 = img.copy()

print(id(img), id(img1), id(img2))

img1[100:200, 100:200] = [0, 0, 255]

cv.imshow('img1', img1)
cv.imshow('img2', img2)

cv.waitKey(0)
cv.destroyAllWindows()

