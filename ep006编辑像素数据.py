# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep006编辑像素数据.py
    @时间：2024/2/20 11:29
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np

img = cv.imread('lena_copy.jpg', flags=1)

x, y, z = img.shape
print(x, y, z)

# 访问像素值
m, n = 100, 100
B, G, R = img[m, n]
print("B:{}, G:{}, R:{}".format(B, G, R))

# 修改像素值
img[m, n] = [255, 255, 255]
B, G, R = img[m, n]
print("B:{}, G:{}, R:{}".format(B, G, R))

#  修改像素值
img[100:200, 100:200, :] = 0
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()

