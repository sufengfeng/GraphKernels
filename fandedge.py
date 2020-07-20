#!/usr/bin/python3
# -*- coding:utf-8 -*-
from dataset import DataSet

# 寻找最适合边


# 测试了好几种方法，
# 1、尝试了graphkernels
# 2、坐标点完全填充为图像，根据shift特征求相似度 ，
# 3、坐标点连线保存为图像，根据gabor特征求相似度，
# 4、最后是目前方法，比较简单，但是挺有效果的。
from points_compare import GetPonints2DistanceList, getDifferenceSum

MatchLine = 15


# 查找数组中是否有匹配的边
def IsMatch(edge, edgeList):
    for j in range(len(edgeList)):
        difference = abs(edge - edgeList[j])
        if difference < MatchLine:
            return True
    return False


# 遍历listA中所有边，查找listB中是否存在存在对应的边
def FindBestMatch(listA, listB):
    # currentMarkList=[]      #记录已匹配ddge
    # currentMarkList.append(j)
    for i in range(len(listA)):
        isMatched = IsMatch(listA[i], listB)
        if isMatched == False:
            return False
    return True


AdvanceMatchLine = 40


def IsOnlyMatch(edge, edgeList, currentMatchList):
    for j in range(len(edgeList)):
        if j in currentMatchList:  # 如果存在已匹配列表中，则跳过
            continue
        difference = abs(edge - edgeList[j])
        if difference < AdvanceMatchLine:
            currentMatchList.append(j)
            return True
    return False


# 遍历listA中所有边，查找listB中是否存在且唯一存在对应的边
# 增加唯一性条件，进行更精准的匹配，
def FindBestMatchAdvance(listA, listB):
    currentMarkList = []  # 记录已匹配ddge
    for i in range(len(listA)):
        isMatched = IsOnlyMatch(listA[i], listB, currentMarkList)
        if isMatched == False:
            return False
    return True


if __name__ == "__main__":
    graphDiatanceList = []
    for i in range(len(DataSet)):  # 10类数据
        categaryDataSet = DataSet[i]
        for j in range(len(categaryDataSet)):
            pointsList = categaryDataSet[j]
            distanceList = GetPonints2DistanceList(pointsList)
            graphDiatanceList.append(distanceList)
        # print(graphDiatanceList)

    print(
        "************************************************************************************************************")

    # 基于所有edge差值之和的判别，效果不行
    # for i in range(len(graphDiatanceList)):
    #     for j in range(len(graphDiatanceList)):
    #         print('Categary_%d_Num%d与Categary_%d_Num%d:%f' % (i / 5, i % 5, j / 5, j % 5, getDifferenceSum(graphDiatanceList[i], graphDiatanceList[j])))
    #     print('*******************************************************************')

    # #基于最小差值的判别
    # for i in range(len(graphDiatanceList)):
    #     print('*********************************    %d   **********************************' % (i % 10))
    #     for j in range(len(graphDiatanceList)):
    #         print('Categary_%d_Num%d与Categary_%d_Num%d:%d' % (i / 5, i % 5, j / 5, j % 5, FindBestMatch(graphDiatanceList[i], graphDiatanceList[j])))
    # 改进的基于最小差值的判别
    for i in range(len(graphDiatanceList)):
        print('*********************************    %d   **********************************' % (i % 10))
        for j in range(len(graphDiatanceList)):
            print('Categary_%d_Num%d与Categary_%d_Num%d:%d' % (i / 5, i % 5, j / 5, j % 5, FindBestMatchAdvance(graphDiatanceList[i], graphDiatanceList[j])))
    # i = 0
    # j = 0
    # print('Categary_%d_Num%d与Categary_%d_Num%d:%d' % (
    # i / 5, i % 5, j / 5, j % 5, FindBestMatchAdvance(graphDiatanceList[i], graphDiatanceList[j])))
    # i = 0
    # j = 2
    # print('Categary_%d_Num%d与Categary_%d_Num%d:%d' % (
    # i / 5, i % 5, j / 5, j % 5, FindBestMatchAdvance(graphDiatanceList[i], graphDiatanceList[j])))
    # i = 0
    # j = 10
    # print('Categary_%d_Num%d与Categary_%d_Num%d:%d' % (
    # i / 5, i % 5, j / 5, j % 5, FindBestMatchAdvance(graphDiatanceList[i], graphDiatanceList[j])))

    # FindBestMatch(graphDiatanceList[0],graphDiatanceList[1])
    print("debug")
    print("debug")
