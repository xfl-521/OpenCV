# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep014图像渐变拼接算法.py
    @时间：2024/2/21 16:39
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np

img1 = cv.imread('lena_copy.jpg')
img2 = cv.imread("flowers.jpg")

wList = np.arange(0.0, 1.0, 0.02)  # start, end, step

for w in wList:
    imgAddW = cv.addWeighted(img1, w, img2, (1 - w), 0)
    cv.imshow("imgAddWeight", imgAddW)
    cv.waitKey(100)

cv.destroyAllWindows()