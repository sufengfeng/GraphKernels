#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

import numpy as np
import graphkernels.kernels as gk

from dataset import DataSet
from get_graphs_list import GetGraphList

if __name__ == "__main__":
    catagrateryGraphList=[]
    for i in range(len(DataSet)):  # 10类数据
        pointsGraphList = []
        pointsGraphList=GetGraphList(DataSet[i])#获得单类的图列表
        catagrateryGraphList.append(pointsGraphList)
    print catagrateryGraphList

    sum_Graphlist=[]
    for i in range(len(catagrateryGraphList)):
        for j in range(len(catagrateryGraphList[i])):
            sum_Graphlist.append(catagrateryGraphList[i][j])

    mutag_list=np.array(sum_Graphlist)
    ### ALL KERNELS COMPUTE
    K1 = gk.CalculateEdgeHistKernel(mutag_list)
    K2 = gk.CalculateVertexHistKernel(mutag_list)
    K3 = gk.CalculateVertexEdgeHistKernel(mutag_list)
    K4 = gk.CalculateVertexVertexEdgeHistKernel(mutag_list)
    K5 = gk.CalculateEdgeHistGaussKernel(mutag_list)
    K6 = gk.CalculateVertexHistGaussKernel(mutag_list)
    K7 = gk.CalculateVertexEdgeHistGaussKernel(mutag_list)
    # K8 = gk.CalculateGeometricRandomWalkKernel(mutag_list)
    # K9 = gk.CalculateExponentialRandomWalkKernel(mutag_list)
    K10 = gk.CalculateKStepRandomWalkKernel(mutag_list)
    K11 = gk.CalculateWLKernel(mutag_list)
    K12 = gk.CalculateConnectedGraphletKernel(mutag_list, 4)
    K13 = gk.CalculateGraphletKernel(mutag_list, 4)
    # K14 = gk.CalculateShortestPathKernel(mutag_list)
    #获得10类，50种图，计算相识度
    pass
