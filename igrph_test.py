#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

import igraph

# 1.
print(igraph.__version__)  # 版本
g = igraph.Graph(1)
print(g)  # g是图的对象
g.add_vertices(3)  # 增加3个顶点
print(g)
g.add_edges([(0, 1), (1, 2), (0, 2), (1, 3), (0, 3), (2, 3)])  # 加边
print(g)

file = open("01.igraphaTest.txt", "w")  # 写入文件
g.write_pajek(file)
file.close()
# IGRAPH U--- 3 3 -- 三个顶点 三个边长

# 2.
g = igraph.Graph([(0, 2), (0, 3), (3, 1), (3, 4), (3, 5), (1, 4)])  # 创建图
print(g)
print(g.degree())  # 每个点与其他几个点有关系
print(igraph.summary(g))  # 概述<br><br>#3.