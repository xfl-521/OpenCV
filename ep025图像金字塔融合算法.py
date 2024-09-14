# -*- coding: utf-8 -*-
"""
-------------------------------
    @软件：PyCharm
    @PyCharm：2023
    @Python：3.8
    @项目：opencv
-------------------------------
    @文件：ep025图像金字塔融合算法.py
    @时间：2024/2/26 21:55
    @作者：XFK
    @邮箱：fkxing2000@163.com
# -------------------------------
"""
import cv2
import numpy as np

A = cv2.imread('Apple.png')
A = cv2.resize(A, (512, 512), interpolation=cv2.INTER_CUBIC)
B = cv2.imread('Orange.png')
B = cv2.resize(B, (512, 512), interpolation=cv2.INTER_CUBIC)

# 生成8层的高斯金字塔gpA
G = A.copy()
gpA = [G]
for i in range(7):
    # 进行7次高斯模糊+下采样
    G = cv2.pyrDown(G)
    # 把每次高斯模糊+下采样的结果送给gpA
    gpA.append(G)

# 生成8层的高斯金字塔gpB
G = B.copy()
gpB = [G]
for i in range(7):
    # 进行7次高斯模糊+下采样
    G = cv2.pyrDown(G)
    # 把每次高斯模糊+下采样的结果送给gpB
    gpB.append(G)

# 把两个高斯金字塔进行合并
LR = []
# zip(lpA,lpB)把两个高斯金字塔各层的两个图像组合成一个元组，然后各元组构成一个大zip
# 对于各元组中的两个图像
for la, lb in zip(gpA, gpB):
    # 取la或lb的尺寸皆可
    rows, cols, dpt = la.shape
    # 利用np.hstack将这两个图像“一半一半”地拼接起来
    # 取la的左边一半和lb的右边一半拼成一个融合后的图，结果赋给ls
    lr = np.hstack((la[:, 0:cols // 2], lb[:, cols // 2:]))
    # 两个拉普拉斯金字塔各层图像融合后的结果赋给LS
    LR.append(lr)

# 用融合后的拉普拉斯金字塔重构出最终图像
# 初始化ls为融合后拉普拉斯金字塔的最高层
# 下面的循环结束后ls就是要求的最终结果图像
lr = LR[7]
for i in range(6, -1, -1):
    # 每层图像先上采样，再和当前层的下一层图像相加，结果再赋给ls
    lr = cv2.pyrUp(lr)
    lr = cv2.add(lr, LR[i])
# ---------------------------------------------------------------------------------------------------
# 生成8层拉普拉斯金字塔
# 从顶层开始构建
# 顶层即高斯金字塔的顶层
lpA = [gpA[7]]
# 7 6 5 4 3 2 1
for i in range(7, 0, -1):
    # 从顶层开始，不断上采样
    GE = cv2.pyrUp(gpA[i])
    # 用下一层的高斯减去上层高斯的上采样
    L = cv2.subtract(gpA[i - 1], GE)
    # 结果送给拉普拉斯金字塔
    lpA.append(L)

lpB = [gpB[7]]
for i in range(7, 0, -1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i - 1], GE)
    lpB.append(L)

# 把两个拉普拉斯金字塔进行合并
LS = []
# zip(lpA,lpB)把两个拉普拉斯金字塔各层的两个图像组合成一个元组，然后各元组构成一个大zip
# 对于各元组中的两个图像
for la, lb in zip(lpA, lpB):
    # 取la或lb的尺寸皆可
    rows, cols, dpt = la.shape
    # 利用np.hstack将这两个图像“一半一半”地拼接起来
    # 取la的左边一半和lb的右边一半拼成一个融合后的图，结果赋给ls
    ls = np.hstack((la[:, 0:cols // 2], lb[:, cols // 2:]))
    # 两个拉普拉斯金字塔各层图像融合后的结果赋给LS
    LS.append(ls)

# 用融合后的拉普拉斯金字塔重构出最终图像
# 初始化ls为融合后拉普拉斯金字塔的最高层
# 下面的循环结束后ls就是要求的最终结果图像
ls = LS[0]
for i in range(1, 8):
    # 每层图像先上采样，再和当前层的下一层图像相加，结果再赋给ls
    ls = cv2.pyrUp(ls)
    ls = cv2.add(ls, LS[i])

with_pyramid = lr + ls

without_pyramid = np.hstack((A[:, :cols // 2], B[:, cols // 2:]))

cv2.imshow("with_pyramid", with_pyramid)
cv2.imshow("without_pyramid", without_pyramid)
cv2.waitKey(0)
cv2.destroyAllWindows()

