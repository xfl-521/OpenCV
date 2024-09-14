# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep001读入显示图像.py
    @时间：2024/2/20 10:51
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv

img = cv.imread('lena.png')
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
