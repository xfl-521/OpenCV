# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep018图像叠加.py
    @时间：2024/2/21 17:42
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('lena_copy.jpg')  # 读取彩色图像(BGR)
img2 = cv2.imread('opencv-lgcopy.jpg')  # 读取 CV Logo

x, y = (10, 10)  # 图像叠加位置
img2 = cv2.resize(img2, (100, 100))
W1, H1 = img1.shape[1::-1]
W2, H2 = img2.shape[1::-1]

imgROI = img1[y:y + H2, x:x + W2]  # 从背景图像裁剪出叠加区域图像

img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # img2: 转换为灰度图像
ret, mask = cv2.threshold(img2Gray, 175, 255, cv2.THRESH_BINARY)  # 转换为二值图像，生成遮罩，LOGO 区域黑色遮盖
maskInv = cv2.bitwise_not(mask)  # 按位非(黑白转置)，生成逆遮罩，LOGO 区域白色开窗，LOGO 以外区域黑色

# mask 黑色遮盖区域输出为黑色，mask 白色开窗区域与运算（原图像素不变）
img1Bg = cv2.bitwise_and(imgROI, imgROI, mask=mask)  # 生成背景，imgROI 的遮罩区域输出黑色
img2Fg = cv2.bitwise_and(img2, img2, mask=maskInv)  # 生成前景，LOGO 的逆遮罩区域输出黑色

imgROIAdd = cv2.add(img1Bg, img2Fg)  # 前景与背景合成，得到裁剪部分的叠加图像
imgAdd = img1.copy()
imgAdd[y:y + H2, x:x + W2] = imgROIAdd  # 用叠加图像替换背景图像中的叠加位置，得到叠加 Logo 合成图像

plt.figure(figsize=(9, 6))
titleList = ["1. imgGray", "2. imgMask", "3. MaskInv", "4. img2FG", "5. img1BG", "6. imgROIAdd"]
imageList = [img2Gray, mask, maskInv, img2Fg, img1Bg, imgROIAdd]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.title(titleList[i]), plt.axis('off')
    if imageList[i].ndim == 3:  # 彩色图像 ndim=3
        plt.imshow(cv2.cvtColor(imageList[i], cv2.COLOR_BGR2RGB))  # 彩色图像需要转换为 RGB 格式
    else:  # 灰度图像 ndim=2
        plt.imshow(imageList[i], 'gray')
plt.show()
cv2.imshow("imgAdd", imgAdd)  # 显示叠加图像 imgAdd
cv2.waitKey(0)
cv2.destroyAllWindows()
