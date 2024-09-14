# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep023图像尺寸调整.py
    @时间：2024/2/26 18:40
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('lena_copy.jpg', flags=1)

# 根据缩放比例
rate = 0.5
res = cv.resize(img, None, fx=rate, fy=rate, interpolation=cv.INTER_CUBIC)
# 插值算法选择，如果要缩小图像，推荐使用INTER_AREA插值效果最好，如果要放大图像，INTER_CUBIC效果最好，但是速度较慢，可以考虑使用INTER_LINEAR速度较快，效果也还不错。

# 指定图像尺寸
size = 300
res2 = cv.resize(img, (size, size), interpolation=cv.INTER_CUBIC)

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.axis('on'), plt.title('ORIGINAL'), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.subplot(132), plt.axis('on'), plt.title('RESIZE'), plt.imshow(cv.cvtColor(res, cv.COLOR_BGR2RGB))
plt.subplot(133), plt.axis('on'), plt.title('RESIZE2'), plt.imshow(cv.cvtColor(res2, cv.COLOR_BGR2RGB))
plt.show()
