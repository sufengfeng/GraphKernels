import numpy as np
import cv2
import sys
import pHash_hanming
import os
import pickle

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


# 不用 Gabor滤波过滤 而直接使用感知hash算法 效果要更好


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


if __name__ == '__main__':
    # demo()
    # 读取数据
    filters = build_filters()
    image_path = '../BMP600/'
    pickle_data_path = './image_pHash'
    image_pHash = {}
    if os.path.exists(pickle_data_path):
        with open(pickle_data_path, 'rb') as f:
            image_pHash = pickle.load(f, encoding='UTF_8')
    if image_pHash is None or len(image_pHash) == 0:
        filenames = os.listdir(image_path)
        for f in filenames:
            if f[:3] not in image_pHash.keys():
                image_pHash[f[:3]] = []
            image_pHash[f[:3]].append(
                pHash_hanming.pHash_hexadeclimal(process(cv2.imread(image_path + f, cv2.IMREAD_GRAYSCALE), filters)))
        with open(pickle_data_path, 'wb') as f:
            pickle.dump(image_pHash, f)

    # 处理数据 计算 相似度
    print('图片001_1.bmp 与图片001_*.bmp 的相似度：')
    phash_001 = image_pHash['001'][0]
    for i in range(len(image_pHash['001'])):
        print("%s : %s" % (
            i + 1, pHash_hanming.similarity(pHash_hanming.count_hanming(phash_001, image_pHash['001'][i]))))

    print('图片001_1.bmp 与图片002_*.bmp 的相似度：')
    for i in range(len(image_pHash['002'])):
        print("%s : %s" % (
            i + 1, pHash_hanming.similarity(pHash_hanming.count_hanming(phash_001, image_pHash['002'][i]))))
