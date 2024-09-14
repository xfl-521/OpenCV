# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep010图像拼接.py
    @时间：2024/2/20 15:18
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np

img = cv.imread('lena_copy.jpg')

img1 = img.copy()
img1 = cv.cvtColor(img1, cv.COLOR_BGR2HSV)

img = cv.resize(img, (300, 300))
img1 = cv.resize(img1, (300, 300))
# 水平拼接
img2 = np.hstack((img, img1))
# 垂直拼接
img3 = np.vstack((img, img1))

imgStackH = cv.hconcat((img, img1))
imgStackV = cv.vconcat((img, img1))

cv.imshow("DemoStackH", imgStackH)
cv.imshow("DemoStackV", imgStackV)
cv.imshow('image', img2)
cv.imshow('image1', img3)
cv.waitKey(0)
cv.destroyAllWindows()
