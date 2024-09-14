# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep024图像金字塔.py
    @时间：2024/2/26 19:50
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np

img = cv.imread('lena_copy.jpg', flags=1)
img1 = cv.imread('flowers.jpg', flags=1)

img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_LINEAR)

# 创建图像金字塔（上采样）
pyramid_up = [img]
for i in range(3):  # 根据需要调整金字塔层级数
    img = cv.pyrUp(img)
    pyramid_up.append(img)

# 创建图像金字塔（下采样）
pyramid_down = [img]
for i in range(3):  # 根据需要调整金字塔层级数
    img = cv.pyrDown(img)
    pyramid_down.append(img)

# 显示图像金字塔
for i, img in enumerate(pyramid_up):
    cv.imshow(f'Up Pyramid Level {i}', img)

for i, img in enumerate(pyramid_down[::-1]):
    cv.imshow(f'Down Pyramid Level {i}', img)

cv.waitKey(0)
cv.destroyAllWindows()