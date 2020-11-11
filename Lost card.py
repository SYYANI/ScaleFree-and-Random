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
import matplotlib.pyplot as plt
import copy

# ____________________________________________________________________
# SECTION 2 - CREATING PHOTO

final_nodes2 = 500#int(input("Please type in the final number of nodes: "))
m_parameter2 = 20#int(input("\nPlease type in the least number of each nood connected: "))
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

# ____________________________________________________________________
# SECTION 3 - ALGORITHM
node_con=[]
Connet_Nodes=[]    
def Read_list(filename):
    file1 = open(filename+".txt", "r")
    list_row =file1.readlines()
    list_source = []
    for i in range(len(list_row)):
        column_list = list_row[i].strip().split("\t") 
        list_source.append(column_list)                
    for i in range(len(list_source)):  
        for j in range(len(list_source[i])):  
            if list_source[i][j]!='':
                list_source[i][j]=int(list_source[i][j])
    file1.close()
    return list_source
def Save_list(list1,filename):
    file2 = open(filename + '.txt', 'w')
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            file2.write(str(list1[i][j]))             
            file2.write('\t')                      
        file2.write('\n')                          
    file2.close()
#lists=node_con
#Save_list(lists,'net_k')#保存二维列表到文件
node_con=Read_list('net_k')#从文件中读取二维列表
    
    
node_conn=copy.deepcopy(node_con) 

#for j1 in range(len(G2.nodes())):   
Connet_Nodes=node_con
 
for jk in range(len(G2.nodes())):
    j3=0
    for j2 in Connet_Nodes[jk]:
        Connet_Nodes[jk][j3]=node_conn[j2]
        j3+=1
path=[]

PN1 =random.randint(0,final_nodes2)#int(input("\nThe first person's number(small than {}): ".format(final_nodes2)))
PN2 =random.randint(0,final_nodes2)#int(input("\nThe second person's number(small than {}): ".format(final_nodes2)))   

if PN1==PN2:
        path.append([(PN1,PN2)])
else:
    js=0
    for bl in Connet_Nodes[PN1]:
        js+=1
        for blk in bl:
            if blk==PN2:
                path.append([(PN1,node_conn[PN1][js-1]),(node_conn[PN1][js-1],blk)])
            else:
                if blk in node_conn[PN2]:
                    path.append([(PN1,node_conn[PN1][js-1]),(node_conn[PN1][js-1],blk),(PN2,blk)])
                else:
                    js2=0
                    for bl2 in Connet_Nodes[PN2]:
                        js2+=1
                        for bl2k in bl2:
                            if blk==bl2k:
                                path.append([(PN1,node_conn[PN1][js-1]),(node_conn[PN1][js-1],blk),(node_conn[PN2][js2-1],bl2k),(node_conn[PN2][js2-1],PN2)])

node_lists_community1 = [PN1,PN2]
# ____________________________________________________________________
# SECTION 4 - VISUALATION
if len(path)==0:
    print ("Cant Find")
else:
    edge_lists=[]
    edge_lists=min(path, key=len)
    
    print("\n")
    print(min(path, key=len))
    print("You can get to know him only by knowing {} people".format(len(edge_lists)-1))
    pos = nx.spring_layout(G2)
        
    
    plt.figure(figsize=(25, 25))
    nx.draw(G2,pos,node_size=40, with_labels=0, alpha=0.6, node_color="#40a6d1", edge_color="#52bced",whic=2)
    plt.title("Visulation Of Erdos-Renyi Network(Number: {})".format(len(G2.nodes())))
    nx.draw_networkx_nodes(G2,pos,nodelist=node_lists_community1, node_color='r',node_size=40)
    nx.draw_networkx_edges(G2, pos,edgelist=edge_lists,edge_color='r',width=1)

 

