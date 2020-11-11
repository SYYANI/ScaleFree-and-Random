#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 22:21:29 2020

@author: sunyiyan
"""
# ____________________________________________________________________
# SECTION 1 - IMPORTS
import networkx as nx
import numpy as np
import random
import copy

# ____________________________________________________________________
# SECTION 2 - GET_NETWORK_DATA
# 读文件里面的数据转化为二维列表
def Read_list(filename):
    file1 = open(filename+".txt", "r")
    list_row =file1.readlines()
    list_source = []
    for i in range(len(list_row)):
        column_list = list_row[i].strip().split("\t")  # 每一行split后是一个列表
        list_source.append(column_list)                # 在末尾追加到list_source
    for i in range(len(list_source)):  # 行数
        for j in range(len(list_source[i])):  # 列数
            if list_source[i][j]!='':
                list_source[i][j]=int(list_source[i][j])
    file1.close()
    return list_source
#保存二维列表到文件
def Save_list(list1,filename):
    file2 = open(filename + '.txt', 'w')
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            file2.write(str(list1[i][j]))              # write函数不能写int类型的参数，所以使用str()转化
            file2.write('\t')                          # 相当于Tab一下，换一个单元格
        file2.write('\n')                              # 写完一行立马换行
    file2.close()
#lists=node_connn
#Save_list(lists,'3')
node_conn=Read_list('net')


#PN1 =87#random.randint(0,final_nodes2)#int(input("\nThe first person's number(small than {}): ".format(final_nodes2)))
PN1 =int(input("\nThe person's number(small than 2000): "))

# ____________________________________________________________________
# SECTION 3 - ALGORITHM
nud_sum=len(node_conn[PN1])#G2.degree(PN1)
for qs1 in node_conn[PN1]:
    if PN1 in node_conn[qs1]:
        nud_sum+=len(node_conn[qs1])-1#G2.degree[qs1]-1
    else:
        nud_sum+=len(node_conn[qs1])-1#G2.degree[qs1]-1
    for qs2 in node_conn[qs1]:
        if PN1 in node_conn[qs2]:
            count=0
            for qw1 in node_conn[qs2]:
                if PN1 == qw1:
                    count+=1;
            nud_sum+=len(node_conn[qs2])-count#G2.degree[qs2]-count
        else:
            nud_sum+=len(node_conn[qs2])#G2.degree[qs2]
        for qs3 in node_conn[qs2]:
            if PN1 in node_conn[qs3]:
                count=0
                for qw2 in node_conn[qs3]:
                    if PN1 == qw2:
                        count+=1;
                nud_sum+=len(node_conn[qs3])-count#G2.degree[qs3]-count
            else:
                nud_sum+=len(node_conn[qs3])-count#G2.degree[qs3]
print("There will be {} people know about his invention".format(nud_sum))


 

