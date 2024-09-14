# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep028图像投影变换.py
    @时间：2024/2/27 18:37
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('lena_copy.jpg', flags=1)
h, w = img.shape[:2]  # 图片的高度和宽度

pointSrc = np.float32([[0, 0], [w, 0], [0, h], [w, h]])  # 原始图像中4点坐标
pointDst = np.float32([[int(w / 3), int(h / 3)], [int(w * 2 / 3), int(h / 3)], [0, h], [w, h]])  # 变换图像中4点坐标

MP = cv.getPerspectiveTransform(pointSrc, pointDst)  # 计算投影变换矩阵 M
imgP = cv.warpPerspective(img, MP, (w, h), flags=cv.INTER_AREA, borderMode=cv.BORDER_REPLICATE)

plt.figure(figsize=(9, 6))
plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title("Original"), plt.axis('off')
plt.subplot(122), plt.imshow(cv.cvtColor(imgP, cv.COLOR_BGR2RGB)), plt.title("Projective"), plt.axis('off')
plt.show()

