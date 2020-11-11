#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 22:21:29 2020

@author: sunyiyan
"""
import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
import copy

final_nodes2 = int(input("Please type in the final number of nodes: "))
m_parameter2 = 5#int(input("\nPlease type in the least number of each nood connected: "))

link_possible = 0.7#float(input("\nPlease type in the probability that the two nodes can be connected(0～1): "))
    
#节点连接的可能性阈值 即每对节点连接上的可能性均为用户所指定的值
while (link_possible<=0 or link_possible>=1):
    link_possible = float(input("\nWring Input!Please type in the probability again: "))
#确保概率为0～1范围内的值
   
G2 = nx.Graph()

print("Graph created. Number of nodes: {}".format(len(G2.nodes())))
print("Adding nodes...")

def rand_prob_node2():
    random_proba_node2 = np.random.choice(G2.nodes())
    #从网络中的节点列表(G.nodes())中中随机抽取节点 并作为函数的返回值
    return random_proba_node2

def add_edge2():
        if len(G2.edges()) == 0:
            random_proba_node2 = 0
        else:
            random_proba_node2 = rand_prob_node2()
        new_edge2 = (random_proba_node2, new_node2)
        if new_edge2 in G2.edges():
            print("\tThe edge connecting node {} and node {} already exists！".format(new_node2 + 1, random_proba_node2))
            add_edge2()
        else:
            if (random.random()<=link_possible):
                G2.add_edge(new_node2, random_proba_node2)

count = 0
new_node2 = 1

node_lists_community1 = []
node_lists_community2 = []
for k in range(2):
    node_lists_community1.append(k)
for k in range(final_nodes2-2):
    l=k+2
    node_lists_community2.append(l)
all_nodes = node_lists_community1+ node_lists_community2

for h in all_nodes:
#进行指定次数的循环来创造用户指定数目的节点的建立
    G2.add_node(h)
    #用进行的循环次数作为新节点的序号
    count += 1
print("Connect nodes...")
for k in range(final_nodes2-1+5):
    for e in range(0, m_parameter2):
        add_edge2()
    new_node2 += 1
    
print("\nFinal number of nodes ({}) reached".format(len(G2.nodes())))

node_con=[]
for i in range(10000):
    node_con.append([])
temp=[]
for i in range(10000):
    temp.append([])
temp1=[]    
for i in range(10000):
    temp1.append(temp)

Connet_Nodes=[]
for i in range(10000):
    Connet_Nodes.append(temp1)
 
for jsd, nbrs in G2.adjacency():
    node_con[jsd]=list(nbrs.keys()) 
    
node_conn=copy.deepcopy(node_con) 

for j1 in range(len(G2.nodes())):   
    Connet_Nodes[j1]=node_con[j1]
 
for jk in range(len(G2.nodes())):
    j3=0
    for j2 in Connet_Nodes[jk]:
        Connet_Nodes[jk][j3]=node_conn[j2]
        j3+=1
path=[]



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
lists=node_conn
Save_list(lists,'net')
#node_conn=Read_list('1')



PN1 =random.randint(0,final_nodes2)#int(input("\nThe first person's number(small than {}): ".format(final_nodes2)))
PN2 =random.randint(0,final_nodes2)#int(input("\nThe second person's number(small than {}): ".format(final_nodes2)))   


#PN1 = random.randint(0,final_nodes2)#int(input("\nThe first person's number(small than {}): ".format(final_nodes2)))
#PN1 = int(input("\nThe person's number(small than 2000): "))
#会连接到多少个节点

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

 

