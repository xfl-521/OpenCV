# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep016图像绘制形状.py
    @时间：2024/2/21 16:57
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np

img = cv.imread('lena_copy.jpg', flags=1)
mask = np.zeros(img.shape[:2], np.uint8)
# 在图像上做标记
img1 = img.copy()
cv.drawMarker(img1, (300, 300), (20,120,50), markerType=cv.MARKER_TILTED_CROSS, markerSize=20, thickness=5)

# 在图像上绘制一个圆形
cv.circle(mask, (150, 150), 100, 255, -1)  # （图像，位置，半径，颜色，线宽（-1为填充））
cv.circle(img, (350, 150), 50, color=(120, 50, 30), thickness=5)
# 在图像上绘制一条直线
cv.line(mask, (100, 100), (300, 300), 255, 2, lineType=cv.LINE_AA)
cv.line(img, (100, 100), (300, 300), (0, 255, 0), 2)
# 在图像上绘制一个矩形
cv.rectangle(mask, (200, 200), (400, 400), 255, -1)
cv.rectangle(img, (200, 200), (400, 400), (0, 0, 255), 2)

cv.imshow('mask', mask)
cv.imshow('img', img)
cv.imshow('img1', img1)
cv.waitKey(0)
cv.destroyAllWindows()