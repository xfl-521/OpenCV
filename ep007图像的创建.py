# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep007图像的创建.py
    @时间：2024/2/20 11:49
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np

'''
data = np.empty(shape=(225, 225, 3), dtype=np.uint8)
print(data)

data1 = np.zeros(shape=(225, 225, 3), dtype=np.uint8)
print(data1)

data2 = np.ones(shape=(225, 225, 3), dtype=np.uint8)
print(data2)

data3 = np.full(shape=(225, 225, 3), fill_value=255, dtype=np.uint8)
print(data3)
'''

img = cv.imread('lena_copy.jpg', flags=1)

print(img.shape)

new_img = np.zeros_like(img)
print(new_img.shape)

new_img1 = np.full_like(img, 100)

cv.imshow('img', img)
cv.imshow('new_img', new_img)

cv.waitKey(0)
cv.destroyAllWindows()