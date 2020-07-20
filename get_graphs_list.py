#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

import os, sys
from igraph import Graph
from xml.etree import ElementTree as ET

from get_distance import GetPointsAarry

TMP_FILE_NAME = "/tmp/mutag.xml"
# TMP_FILE_NAME = "mutag.xml"
reload(sys)
sys.setdefaultencoding('utf8')


# 创建的目录
path = "/tmp/graph"
if os.path.exists(path)==False:
    os.mkdir( path, 0755 )

def prettyXml(element, indent, newline, level=0):  # elemnt为传进来的Elment类，参数indent用于缩进，newline用于换行
    if len(element):  # 判断element是否有子元素
        if element.text == None or element.text.isspace():  # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
    # else:  # 此处两行如果把注释去掉，Element的text也会另起一行
    # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
    temp = list(element)  # 将elemnt转成list
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):  # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
            subelement.tail = newline + indent * (level + 1)
        else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个
            subelement.tail = newline + indent * level
        prettyXml(subelement, indent, newline, level=level + 1)  # 对子元素进行递归操作


Categary = 0
Num = 0


# 根据距离矩阵和点生成graphml
# 可以优化全连接为最小生成树
def GetGraphmlFile(distanceArray, points):
    # etree 生成一个xml
    root = ET.Element('graphml')  # 生成一个节点root
    root.set("xmlns", "http://graphml.graphdrawing.org/xmlns")
    root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    root.set("xsi:schemaLocation",
             "http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd")
    key = ET.SubElement(root, 'key')  # 生成一个字节点下的子节点child1
    key.set("id", "v_label")
    key.set("for", "node")
    key.set("attr.name", "label")
    key.set("attr.type", "double")

    key = ET.SubElement(root, 'key')  # 生成一个字节点下的子节点child1
    key.set("id", "e_label")
    key.set("for", "edge")
    key.set("attr.name", "label")
    key.set("attr.type", "double")

    graph = ET.SubElement(root, 'graph')  # 生成一个字节点下的子节点child1
    graph.set("id", "G")
    graph.set("for", "undirected")
    # node
    for i in range(len(distanceArray)):
        for j in range(len(distanceArray)):
            if i == j:
                continue
            edge = ET.SubElement(graph, 'edge')  # 生成一个字节点下的子节点child1
            edge.set("source", "n%d" % (i))
            edge.set("target", "n%d" % (j))
            data = ET.SubElement(edge, 'data')  # 生成一个字节点下的子节点child1
            data.set("key", "e_label")
            data.text = str(distanceArray[i][j])
    # edge
    for i in range(len(points)):
        node = ET.SubElement(graph, 'node')  # 生成一个字节点下的子节点child1

        node.set("id", "n%d" % (i))
        data = ET.SubElement(node, 'data')  # 生成一个字节点下的子节点child1
        data.set("key", "v_label")
        data.text = "1"

    prettyXml(root, '\t', '\n')  # 执行美化方法
    tree = ET.ElementTree(root)  # 生成节点树
    fileName = "/tmp/graph/Categary%d_Num%d.xml" % (Categary, Num)
    tree.write(fileName, encoding='utf-8', xml_declaration=True)  # 将xml文件内容写入到文本文件中,文件格式并不是很漂亮
    # ET.tostring(root)

    # try:
    #     fobj = open(TMP_FILE_NAME, 'r')
    # except IOError, e:
    #     print "*** file open error:", e
    # else:
    #     for eachline in fobj:
    #         print eachline,
    # fobj.close()

    return fileName


def GetGraphList(pointList):
    global Categary, Num

    pointsGraphList = []
    for i in range(len(pointList)):  # 5个图
        distanceArray = GetPointsAarry(pointList[i])  # 获得图的距离矩阵
        graphmlFileName = GetGraphmlFile(distanceArray, pointList[i])  # 将矩阵转换为graphml格式,并生成文件
        pointsGraph = Graph.Read_GraphML(graphmlFileName)  # 读取文件，生成图网络
        pointsGraphList.append(pointsGraph)
        Num = Num + 1
        if Num > 4:
            Num = 0
    Categary = Categary + 1
    return pointsGraphList


if __name__ == "__main__":
    distanceArray = [[0.0, 399.0204961659515, 500.1605551425906, 220.08242757443915, 193.98714165293202],
                     [399.0204961659515, 0.0, 180.81941042547544, 349.8545215239509, 279.9111067819685],
                     [500.1605551425906, 180.81941042547544, 0.0, 511.2831632819867, 326.0603063650401],
                     [220.08242757443915, 349.8545215239509, 511.2831632819867, 0.0, 319.96901844482437],
                     [193.98714165293202, 279.9111067819685, 326.0603063650401, 319.96901844482437, 0.0]]

    points = [[284.1169128417969, 675.3806762695312], [380.3543701171875, 288.1395263671875],
              [558.5081787109375, 257.2060546875], [123.1483154296875, 525.2960815429688],
              [441.0755920410156, 561.3851318359375]]
    fileName = GetGraphmlFile(distanceArray=distanceArray, points=points)
    pointsGraph = Graph.Read_GraphML(fileName)  # 读取文件，生成图网络
    print fileName
