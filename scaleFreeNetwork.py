#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 22:14:01 2020

@author: sunyiyan
"""

class Nood:
    def __init__(self):
        self.connectNum = 0
        self.linkNum = 0
    def connectNood(self,nood):
        self.linkNum += 1
        nood.linkNum += 1
    def addNood(self, nood):
        self.connectNum += 1
        nood.connectNum += 1
        
def chooseNood(edges):
    ranNum=random.randint(0,len(edges)-1)
    return edges[ranNum]

def chooseNood_2(edges):
    numOfEdges = len(edges)
    my_dict = dict()
    sum = 0
    for i in range(numOfEdges):
        my_dict[i] = (sum, sum + edges[i].connectNum)
        sum += edges[i].connectNum
    ranNum = random.randint(1,sum)
    for j in range(numOfEdges):
        if my_dict[j][0]< ranNum <= my_dict[j][1]:
            return edges[j]
        
def draw(edges):
    numToconnection_dict = dict()
    while edges:
        lastNood = edges.pop()
        if lastNood.linkNum in numToconnection_dict.keys():
            numToconnection_dict[lastNood.linkNum] += 1
        else:
            numToconnection_dict[lastNood.linkNum] = 1
        
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.set_title("Erdos-Renyi Random Network",fontsize=24)
    ax.set_xlabel("Number of connections",fontsize=14)
    ax.set_ylabel("Number",fontsize=14)
    ax.scatter(numToconnection_dict.keys(), numToconnection_dict.values(), s=30)
    
    plt.show()
    
def draw_2(edges):
    numToconnection_dict = dict()
    numToconnection_dict_key = dict()
    while edges:
        lastNood = edges.pop()
        if lastNood.connectNum in numToconnection_dict.keys():
            numToconnection_dict[lastNood.connectNum] += 1
        else:
            numToconnection_dict[lastNood.connectNum] = 1
        
    for key in numToconnection_dict.keys():
        numToconnection_dict[key] = math.log(numToconnection_dict[key], 10)
        numToconnection_dict_key[key]=math.log(key, 10)
        
    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    ax.set_title("Scale Free Network",fontsize=24)
    ax.set_xlabel("lg(Number of connections)",fontsize=14)
    ax.set_ylabel("lg(Number)",fontsize=14)
    ax.scatter(numToconnection_dict_key.values(), numToconnection_dict.values(), s=30)
    plt.show()
    
if __name__ == "__main__":
    import random
    import math
    import matplotlib.pyplot as plt
    
    chooseNumber = int(input("\nchoose Erdos-Renyi model by 1 or Scale-Free model by 2: "))
    
    edges = list()
    nood1, nood2 = Nood(), Nood()
    nood1.addNood(nood2)
    edges.append(nood1)
    edges.append(nood2)
    
    if (chooseNumber==1):
        final_nodes = int(input("\nPlease type in the final number of nodes: "))
        m_parameter = int(input("\nPlease type in the least number of each nood connected: "))
        
        for i in range(final_nodes-2):
            new_nood = Nood()
            edges.append(new_nood)
        
        for i in range(final_nodes):
            for j in range(m_parameter):
                chooseNood(edges).connectNood(edges[i])
        draw(edges)
        
    if (chooseNumber==2):
        final_nodes = int(input("\nPlease type in the final number of nodes: "))
        m_parameter = int(input("\nPlease type in the number of each nood connected when it first came into the network: "))
        for i in range(final_nodes-2):
            new_nood = Nood()
            for j in range(m_parameter):
                chooseNood_2(edges).addNood(new_nood)
            edges.append(new_nood)
        draw_2(edges)

        
        
        
        
        
