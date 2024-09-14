# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep009图像裁切.py
    @时间：2024/2/20 14:55
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2 as cv
import numpy as np

img = cv.imread('opencv-lg.jpg', flags=1)

# 给定参数确定裁切范围
xmin, ymin, w, h = 180, 190, 200, 200
imgCrop = img[ymin:ymin + h, xmin:xmin + w].copy()

# 手动鼠标选择感兴趣区域
roi = cv.selectROI(img, showCrosshair=True, fromCenter=False)
xmin, ymin, w, h = roi  # 矩形裁剪区域 (ymin:ymin+h, xmin:xmin+w) 的位置参数
imgROI = img[ymin:ymin + h, xmin:xmin + w].copy()  # 切片获得裁剪后保留的图像区域

cv.imshow("DemoCrop", imgCrop)
cv.imshow("DemoRIO", imgROI)
cv.waitKey(0)
cv.destroyAllWindows()

