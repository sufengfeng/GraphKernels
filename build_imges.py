#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os

import cv2
import numpy as np

from BasicDataSet import BasicDataSet
#from dataset import DataSet


# 创建的目录
# path = "/tmp/graph"
# if os.path.exists(path)==False:
#     os.mkdir( path, 0755 )

def SaveImages():
    for j in range(len(BasicDataSet)):  # 5个
        points = BasicDataSet[j]
        img = np.zeros((900, 900, 3), np.uint8)
        for k in range(len(points)):
            for m in range(k + 1, len(points)):
                pintA = (int(points[k][0]),int(points[k][1]))
                pintB = (int(points[m][0]), int(points[m][1]))
                cv2.line(img, pintA, pintB, (255, 255, 255), 2, lineType=cv2.LINE_8, shift=0)
        cv2.imwrite('./images/img_Num%d.bmp'%(j), img)
        # cv2.namedWindow('line')
        # cv2.imshow('line', img)
        # cv2.waitKey(1000)  # 显示 10000ms 即10s后消失
        # cv2.destroyAllWindows()

if __name__ == "__main__":
    SaveImages()

    pass
