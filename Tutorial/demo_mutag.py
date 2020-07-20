#!/usr/bin/python2.7
# -*- coding:utf-8 -*-
"""
In this demo we show how to
calculate the kernel matrices
on the MUTAG data
"""

import graphkernels.kernels as gk

import IPython as ip
import numpy as np

# Load data
# comment next line if data.mutag is in a different folder
# mutag_list = np.load("graphkernels/data.mutag")

# Uncomment next line if data.mutag is in your current folder
mutag_list = np.load("data.mutag")


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
print "debug"

###所有内核计算
# 计算边缘历史核
# 计算顶点历史核
# 计算顶点边缘历史核
# 计算顶点顶点边缘历史核
# 计算边缘HistGauss核
# 计算顶点HistGauss内核
# 计算顶点边缘HistGauss内核
# 计算几何随机游走核
# 计算指数随机游走核
# 计算KStep随机游走内核
# 计算WL内核
# 计算ConnectedGraphlet内核
# 计算Graphlet内核
# 计算ShortestPath内核