# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep015图像掩膜加法.py
    @时间：2024/2/21 16:47
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np

img1 = cv.imread('lena_copy.jpg', flags=1)
img2 = cv.imread('flowers.jpg', flags=1)

# 得到一个与图片1尺寸一致的全黑图像
Mask = np.zeros((img1.shape[0], img1.shape[1]), dtype=np.uint8)
#  设置掩膜的 ROI
xmin, ymin, w, h = 150, 150, 200, 200
# ROI赋值为白色，其它区域为黑色
Mask[ymin:ymin + h, xmin:xmin + w] = 255
print(img1.shape, img2.shape, Mask.shape)

imgAddMask1 = cv.add(img1, img2, mask=Mask)  # 带有掩模 mask 的加法
imgAddMask2 = cv.add(img1, np.zeros(np.shape(img1), dtype=np.uint8), mask=Mask)  # 提取 ROI

cv.imshow("MaskImage", Mask)  # 显示掩模图像 Mask
cv.imshow("MaskAdd", imgAddMask1)  # 显示掩模加法结果 imgAddMask1
cv.imshow("MaskROI", imgAddMask2)  # 显示从 img1 提取的 ROI
cv.waitKey(0)
cv.destroyAllWindows()