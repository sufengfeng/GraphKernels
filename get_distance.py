#!/usr/bin/python3
# -*- coding:utf-8 -*-




# 计算点到图中其他点的距离
from points_compare import GetPoint2PonitDistance


def GetPonint2Graph(point, pointList):
    distanceList = []
    for i in range(len(pointList)):
        distance = GetPoint2PonitDistance(point, pointList[i])
        distanceList.append(distance)
    return distanceList


# 得到图中所有距离矩阵
def GetPointsAarry(points):
    distanceArray = []
    for i in range(len(points)):  # 5个点
        distanceList = GetPonint2Graph(points[i], points)
        distanceArray.append(distanceList)
    return distanceArray
