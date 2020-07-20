import numpy as np
from LBP.uniform_pattern_LBP import uniform_pattern_LBP
import cv2


def getLBPH(img_lbp, numPatterns, grid_x, grid_y, normed):
    '''
    计算LBP特征图像的直方图LBPH
    '''
    h, w = img_lbp.shape
    width = int(w / grid_x)
    height = int(h / grid_y)
    # 定义LBPH的行和列，grid_x*grid_y表示将图像分割的块数，numPatterns表示LBP值的模式种类
    result = np.zeros((grid_x * grid_y, numPatterns), dtype=float)
    resultRowIndex = 0
    # 对图像进行分割，分割成grid_x*grid_y块，grid_x，grid_y默认为8
    for i in range(grid_x):
        for j in range(grid_y):
            # 图像分块
            src_cell = img_lbp[i * height:(i + 1) * height, j * width:(j + 1) * width]
            # 计算直方图
            hist_cell = getLocalRegionLBPH(src_cell, 0, (numPatterns - 1), normed)
            # 将直方图放到result中
            result[resultRowIndex] = hist_cell
            resultRowIndex += 1
    return np.reshape(result, (-1))


def getLocalRegionLBPH(src, minValue, maxValue, normed):
    '''
    计算一个LBP特征图像块的直方图
    '''
    data = np.reshape(src, (-1))
    # 计算得到直方图bin的数目，直方图数组的大小
    bins = maxValue - minValue + 1
    # 定义直方图每一维的bin的变化范围
    ranges = (float(minValue), float(maxValue + 1))
    hist, bin_edges = np.histogram(src, bins=bins, range=ranges, normed=normed)
    return hist


if __name__ == '__main__':
    gray = cv2.imread('../BMP600/001_1.bmp', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('img', gray)
    uniform_pattern = uniform_pattern_LBP(gray, 3, 8)
    # uniform_pattern = uniform_pattern_LBP(gray, 3, 8)
    lbph = getLBPH(uniform_pattern, 59, 8, 8, True)
    cv2.imshow('up', uniform_pattern)  # 整体会偏暗
    cv2.waitKey(0)
    cv2.destroyAllWindows()
