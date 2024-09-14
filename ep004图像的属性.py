# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep004图像的属性.py
    @时间：2024/2/20 11:18
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np
# OpenCV 中图像对象的数据结构是 ndarray 多维数组，因此 ndarray 数组的属性和操作方法也都适用于 OpenCV 的图像对象。

img = 'lena_copy.jpg'

# 图像数组的属性
img1 = cv.imread(img, flags=1)  # flags=1 读取彩色图像(BGR)
img2 = cv.imread(img, flags=0)  # flags=0 读取为灰度图像

print(f'原图数据维度：{img1.ndim}，形状：{img1.shape}，元素总数：{img1.size}，元素类型：{img1.dtype}')
print(f'灰度数据维度：{img2.ndim}，形状：{img2.shape}，元素总数：{img2.size}，元素类型：{img2.dtype}')

cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.waitKey(0)
cv.destroyAllWindows()