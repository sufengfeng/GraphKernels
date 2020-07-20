import numpy as np
import cv2
import sys

sys.path.append('../')


def build_filters():
    filters = []
    ksize = 31
    for theta in np.arange(0, np.pi, np.pi / 16):
        kern = cv2.getGaborKernel((ksize, ksize), 4.0, theta, 10.0, 0.5, 0, ktype=cv2.CV_32F)
        kern /= 1.5 * kern.sum()
        filters.append(kern)
    return filters


def process(img, filters):
    accum = np.zeros_like(img)
    for kern in filters:
        fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
        np.maximum(accum, fimg, accum)
    return accum


def demo():
    img_fn = '../BMP600/001_1.bmp'

    img = cv2.imread(img_fn)
    if img is None:
        print('Failed to load image file:', img_fn)
        sys.exit(1)

    filters = build_filters()

    res1 = process(img, filters)
    cv2.imshow('origin', img)
    cv2.imshow('result', res1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_cos(vector_a, vector_b):
    vector_a = np.reshape(vector_a, (-1))
    vector_b = np.reshape(vector_b, (-1))
    num = np.dot(vector_a, vector_b.T)  # 若为行向量则 A * B.T
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom  # 余弦值
    sim = 0.5 + 0.5 * cos  # 归一化
    return sim
