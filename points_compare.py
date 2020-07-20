#!/usr/bin/python3
# -*- coding:utf-8 -*-
from dataset import DataSet


# 求解距离的差值
def getDifferenceSum(listA, listB):
    sumDistance = 0
    for i in range(len(listA)):
        for j in range(len(listB)):
            difference = abs(listA[i] - listB[j])
            sumDistance = sumDistance + difference
    return sumDistance


# 计算点与点之间距离

def GetPoint2PonitDistance(pointA, pointB):
    distance = ((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2) ** 0.5
    return distance


def GetPonints2DistanceList(pointsList):
    pointsDistanceList = []
    for i in range(len(pointsList)):
        for j in range(i + 1, len(pointsList)):
            pointsDistance = GetPoint2PonitDistance(pointsList[i], pointsList[j])
            pointsDistanceList.append(pointsDistance)
    return pointsDistanceList


# 测试了好几种方法，
# 1、尝试了graphkernels
# 2、坐标点完全填充为图像，根据shift特征求相似度 ，
# 3、坐标点连线保存为图像，根据gabor特征求相似度，
# 4、最后是目前方法，比较简单，但是挺有效果的。
if __name__ == "__main__":
    graphDiatanceList = []
    for i in range(len(DataSet)):  # 10类数据
        categaryDataSet = DataSet[i]
        for j in range(len(categaryDataSet)):
            pointsList = categaryDataSet[j]
            distanceList = GetPonints2DistanceList(pointsList)
            graphDiatanceList.append(distanceList)
        print(graphDiatanceList)

    print(
        "************************************************************************************************************")

    for i in range(len(graphDiatanceList)):
        for j in range(len(graphDiatanceList)):
            print('Categary_%d_Num%d与Categary_%d_Num%d:%f' % (i / 5, i % 5, j / 5, j % 5, getDifferenceSum(graphDiatanceList[i], graphDiatanceList[j])))
        print('*******************************************************************')
    print("debug")
    print("debug")
    '''
    # 计算差别
# categary00
    print('Categary_0_Num0 与Categary_0_Num* 的差别：')
    for i in range(5):
        print('Categary_0_Num0与Categary_0_Num%d:%f' % (i, getDifferenceSum(graphDiatanceList[0], graphDiatanceList[i])))
    print('Categary_0_Num0与Categary_1_Num* 的差别：')
    for i in range(5, 10):
        print('Categary_0_Num0与Categary_1_Num%d:%f' % (i, getDifferenceSum(graphDiatanceList[0], graphDiatanceList[i])))
    print('Categary_0_Num0与Categary_2_Num* 的差别：')
    for i in range(10, 15):
        print('Categary_0_Num0与Categary_2_Num%d:%f' % (i, getDifferenceSum(graphDiatanceList[0], graphDiatanceList[i])))
    print("************************************************************************************************************")

# categary02
    print('Categary_2_Num0 与Categary_1_Num* 的差别：')
    for i in range(5):
        print('Categary_2_Num0与Categary_1_Num%d:%f' % (i, getDifferenceSum(graphDiatanceList[10], graphDiatanceList[i])))
    print('Categary_2_Num0与Categary_1_Num* 的差别：')
    for i in range(5, 10):
        print('Categary_2_Num0与Categary_1_Num%d:%f' % (i, getDifferenceSum(graphDiatanceList[10], graphDiatanceList[i])))
    print('Categary_2_Num0与Categary_2_Num* 的差别：')
    for i in range(10, 15):
        print('Categary_2_Num0与Categary_2_Num%d:%f' % (i, getDifferenceSum(graphDiatanceList[10], graphDiatanceList[i])))

    print("************************************************************************************************************")
    '''
