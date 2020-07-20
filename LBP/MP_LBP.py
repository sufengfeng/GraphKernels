import cv2
import numpy as np
from LBP.origin_LBP import origin_LBP


def multi_scale_block_LBP(img, scale):
    h, w = img.shape

    # 定义并计算积分图像
    cellSize = int(scale / 3)
    offset = int(cellSize / 2)
    cellImage = np.zeros((h - 2 * offset, w - 2 * offset), dtype=img.dtype)

    for i in range(offset, h - offset):
        for j in range(offset, w - offset):
            temp = 0
            for m in range(-offset, offset + 1):
                for n in range(-offset, offset + 1):
                    temp += img[i + n, j + m]

            temp /= (cellSize * cellSize)
            cellImage[i - int(cellSize / 2), j - int(cellSize / 2)] = np.uint8(temp)

    dst = origin_LBP(cellImage)
    return dst


if __name__ == '__main__':
    gray = cv2.imread('../BMP600/001_1.bmp', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('img', gray)
    mb_3 = multi_scale_block_LBP(gray, 3)
    mb_9 = multi_scale_block_LBP(gray, 9)
    mb_15 = multi_scale_block_LBP(gray, 15)
    cv2.imshow('mb_3', mb_3)
    cv2.imshow('mb_9', mb_9)
    cv2.imshow('mb_15', mb_15)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
