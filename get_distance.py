#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# 计算点与点之间距离

def GetPoint2PonitDistance(pointA, pointB):
    distance = ((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2) ** 0.5
    return distance


# 计算点到图中其他点的距离

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
