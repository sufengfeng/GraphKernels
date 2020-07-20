import cv2
import numpy as np
import sys

sys.path.append('../')

"""
原始的LBP算子定义为在3∗3的窗口内，以窗口中心像素为阈值，将相邻的8个像素的灰度值与其进行比较，若周围像素值大于等于中心像素值，则该像素点的位置被标记为1，否则为0。
这样，3∗3邻域内的8个点经比较可产生8位二进制数（通常转换为十进制数即LBP码，共256种），即得到该窗口中心像素点的LBP值，并用这个值来反映该区域的纹理信息。需要注意的是，LBP值是按照顺时针方向组成的二进制数。

"""

def origin_LBP(img):
    dst = np.zeros(img.shape, dtype=img.dtype)
    h, w = img.shape
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            center = img[i][j]
            code = 0

            code |= (img[i - 1][j - 1] >= center) << (np.uint8)(7)
            code |= (img[i - 1][j] >= center) << (np.uint8)(6)
            code |= (img[i - 1][j + 1] >= center) << (np.uint8)(5)
            code |= (img[i][j + 1] >= center) << (np.uint8)(4)
            code |= (img[i + 1][j + 1] >= center) << (np.uint8)(3)
            code |= (img[i + 1][j] >= center) << (np.uint8)(2)
            code |= (img[i + 1][j - 1] >= center) << (np.uint8)(1)
            code |= (img[i][j - 1] >= center) << (np.uint8)(0)

            dst[i - 1][j - 1] = code
    return dst


if __name__ == '__main__':
    gray = cv2.imread('../BMP600/001_1.bmp', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('img', gray)
    org_lbp = origin_LBP(gray)
    cv2.imshow('org_lbp', org_lbp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
