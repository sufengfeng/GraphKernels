import numpy as np
import cv2
import sys
import Gabor_common as Gabor
import os
from LBP import LBPH
from LBP.MP_LBP import multi_scale_block_LBP
from LBP.rotation_invariant_LBP import rotation_invariant_LBP
from LBP.uniform_pattern_LBP import uniform_pattern_LBP

sys.path.append('../')


def step_pixel_cos():
    """
    逐像素计算图片经过Gabor滤波转换后的余弦值（有经过归一化处理）
    :return:
    """
    # 读取数据
    filters = Gabor.build_filters()
    image_path = './BMP600/'
    filenames = os.listdir(image_path)
    filenames.sort()
    image_H = np.ndarray(shape=(len(filenames), 128 * 128))
    for i in range(len(filenames)):
        img = cv2.imread(image_path + filenames[i], cv2.IMREAD_GRAYSCALE)
        res1 = Gabor.process(img, filters)
        image_H[i] = res1.reshape((-1))
        # 做归一化处理
        image_H[i] = (image_H[i] - np.mean(image_H[i])) / (np.max(image_H[i]) - np.min(image_H[i]))
        if i == 17:
            break

    # 计算余弦值
    print('图片001_1.bmp 与图片001_*.bmp 的特征向量余弦值：')
    for i in range(6):
        print('001_1.bmp 与001_%d.bmp:%f' % (i + 1, Gabor.get_cos(image_H[0], image_H[i])))
    print('图片001_1.bmp 与图片002_*.bmp 的特征向量余弦值：')
    for i in range(6, 12):
        print('001_1.bmp 与img_Categary_1_Num%d.bmp:%f' % (i + 1, Gabor.get_cos(image_H[0], image_H[i])))
    print('图片001_1.bmp 与图片003_*.bmp 的特征向量余弦值：')
    for i in range(12, 18):
        print('001_1.bmp 与003_%d.bmp:%f' % (i + 1, Gabor.get_cos(image_H[0], image_H[i])))


if __name__ == '__main__':
    # step_pixel_cos()
    # 读取数据
    NUM_PATTERNS = 59
    filters = Gabor.build_filters()
    image_path = './images/'
    filenames = os.listdir(image_path)
    filenames.sort()
    image_H = np.ndarray(shape=(len(filenames), 64 * NUM_PATTERNS))
    for i in range(len(filenames)):
        print(filenames[i])
        img = cv2.imread(image_path + filenames[i], cv2.IMREAD_GRAYSCALE)
        res1 = Gabor.process(img, filters)
        #res1 = img
        #lbp_img = multi_scale_block_LBP(res1, 5)
        lbp_img = rotation_invariant_LBP(res1,radius=10)    #使用旋转不变性
        #lbp_img = uniform_pattern_LBP(res1)  # 使用旋转不变性

        image_H[i] = LBPH.getLBPH(lbp_img, NUM_PATTERNS, 8, 8, False)
        if i == 15:
            break

    # 计算余弦值

    print('img_Categary_0_Num0.bmp 与图片img_Categary_0_Num*.bmp 的特征向量余弦值：')
    for i in range(5):
        print('img_Categary_0_Num0.bmp与img_Categary_0_Num%d.bmp:%f' % (i, Gabor.get_cos(image_H[0], image_H[i])))
    print('图片img_Categary_0_Num0.bmp与图片img_Categary_1_Num*.bmp 的特征向量余弦值：')
    for i in range(5, 10):
        print('img_Categary_0_Num0.bmp与img_Categary_1_Num%d.bmp:%f' % (i, Gabor.get_cos(image_H[0], image_H[i])))
    print('图片img_Categary_0_Num0.bmp与图片img_Categary_2_Num*.bmp 的特征向量余弦值：')
    for i in range(10, 15):
        print('img_Categary_0_Num0.bmp与img_Categary_2_Num%d.bmp:%f' % (i, Gabor.get_cos(image_H[0], image_H[i])))
