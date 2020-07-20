#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

from dataset import DataSet


def ShowPoints():
    # x = np.linspace(0.05, 10, 1000)
    # y = np.cos(x)
    # plt.plot(x, y, ls="-", lw=2, label="plot figure")
    # plt.legend()
    # count=0
    for i in range(len(DataSet)):  # 10类数据
        for j in range(len(DataSet[i])):#5个
            listX=[]
            listY=[]
            for k in range(len(DataSet[i][j])):#5个坐标
                data=DataSet[i][j][k]
                listX.append(data[0])
                listY.append(data[1])
            x=np.array(listX)
            y = np.array(listY)
            plt.plot(x, y,"*", lw=2, label="plot figure")
            #ls="-",
            plt.legend()
            # count=count+1
            # if count>20:
            #     break
        plt.show()


if __name__=="__main__":
    ShowPoints()
    while 1:
        pass