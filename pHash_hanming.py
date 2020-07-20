"""
感知哈希算法的 pHash的实现，提取图片指纹后，使用汉明距离进行图片相似性的比较
加入了余弦变换（余弦哈希感知算法）针对变形，图像角度变换的问题

有image Hash库使用
pip install imagehash
"""

import cv2
import numpy as np
import json

# 图片要被resize到什么shape
RESIZE_First = (64, 64)

RESIZE_Second = (16, 16)


def pHash_binary(img):
    """
    得到图片 二进制字符串的感知余弦哈希 PHash表示
    """
    # 调整图片为灰度图片
    img = cv2.resize(img, RESIZE_First, interpolation=cv2.INTER_CUBIC)
    if len(img.shape) == 3 and img.shape[2] == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 创建二维列表
    h, w = img.shape[:2]
    vis0 = np.zeros((h, w), np.float32)
    vis0[:h, :w] = img  # 填充数据

    # 二维Dct变换
    vis1 = cv2.dct(cv2.dct(vis0))
    # cv.SaveImage('a.jpg',cv.fromarray(vis0)) #保存图片
    vis1 = cv2.resize(vis1, RESIZE_Second, interpolation=cv2.INTER_CUBIC)

    # 把二维list变成一维list
    img_list = np.reshape(vis1, (-1,)).tolist()

    # 计算均值
    avg = sum(img_list) * 1. / len(img_list)
    avg_list = ['0' if i < avg else '1' for i in img_list]

    return avg_list

def pHash_hexadeclimal(img):
    """
    得到图片 十六进制字符串的PHash表示
    """
    avg_list = pHash_binary(img)

    # 得到16进制编码的 哈希值
    return ''.join(
        ['%x' % int(''.join(avg_list[x:x + 4]), 2) for x in range(0, RESIZE_Second[0] * RESIZE_Second[1], 4)])


def str_to_bin(s):
    return ''.join([bin(ord(c)).replace('0b', '') for c in s])


def count_hanming(phash1, phash2):
    """
    计算两张图片的 pHash值的 二进制汉明距离

    Returns:int 汉明距离

    """
    phash1 = str_to_bin(phash1)
    phash2 = str_to_bin(phash2)
    h, d = 0, eval('0b' + phash1) ^ eval('0b' + phash2)
    while d:
        h += 1
        d &= d - 1
    return h


def similarity(hanming_distance):
    all = RESIZE_Second[0] * RESIZE_Second[1]
    return float(all - hanming_distance) / all
