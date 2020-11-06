#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 22:14:01 2020

@author: sunyiyan
"""
# ____________________________________________________________________
# SECTION 1 - IMPORTS

import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt

# ____________________________________________________________________
# SECTION 2 - VISUALISATION FUNCTION

def k_distrib(graph, scale='lin', colour='#40a6d1', alpha=.8, expct_lo=1, expct_hi=10, expct_const=1):
    plt.close()
    num_nodes = graph.number_of_nodes()
    max_degree = 0
    # Calculate the maximum degree to know the range of x-axis
    for n in graph.nodes():
        if graph.degree(n) > max_degree:
            max_degree = graph.degree(n)
    # X-axis and y-axis values
    x = []
    y_tmp = []
    # loop for all degrees until the maximum to compute the portion of nodes for that degree
    for i in range(max_degree+1):
        x.append(i)
        y_tmp.append(0)
        for n in graph.nodes():
            if graph.degree(n) == i:
                y_tmp[i] += 1
        y = [i/num_nodes for i in y_tmp]
    # Plot the graph
    deg, = plt.plot(x, y,label='Degree distribution',linewidth=0, marker='o',markersize=8, color=colour, alpha=alpha)
    # Check for the lin / log parameter and set axes scale
    if scale == 'log':
        plt.xscale('log')
        plt.yscale('log')
        if graph==G:
            plt.title('Scale-Free model Degree distribution (log-log scale)')
        if graph==G2:
            plt.title('Erdos-Renyi model Degree distribution (log-log scale)')
        #plt.title('Degree distribution (log-log scale)')
        # add theoretical distribution line k^-3
        w = [a for a in range(expct_lo,expct_hi)]
        z = []
        for i in w:
            x = (i**-3) * expct_const # set line's length and fit intercept
            z.append(x)

        plt.plot(w,z, 'k-', color='#7f7f7f')
    else:
        if graph==G:
            plt.title('Scale-Free model Degree distribution (linear scale)')
        if graph==G2:
            plt.title('Erdos-Renyi model Degree distribution (linear scale)')


    plt.ylabel('P(k)')
    plt.xlabel('k')
    plt.show()

# ____________________________________________________________________
# SECTION 3 - ALGORITHM

#Choose Model
chooseNumber = int(input("\nchoose Scale-Free model by 1 or Erdos-Renyi model by 2: "))

if chooseNumber==1:
    # Get parameters
    
    init_nodes = int(input("Please type in the initial number of nodes (m_0): "))
    final_nodes = int(input("\nPlease type in the final number of nodes: "))
    m_parameter = int(input("\nPlease type in the least number of each nood connected\n(Less than or equal to 5): "))
    while m_parameter>init_nodes:
        m_parameter = int(input("\nWring Input!Please type in the least number of each nood connected again\n(Less than or equal to 5): "))
    
    print("\n")
    print("Creating initial graph...")
    
    G = nx.complete_graph(init_nodes)
    
    print("Graph created. Number of nodes: {}".format(len(G.nodes())))
    print("Adding nodes...")
    
    def rand_prob_node():
        nodes_probs = []
        for node in G.nodes():
            node_degr = G.degree(node)
            #print(node_degr)
            node_proba = node_degr / (2 * len(G.edges()))
            #Record the degree of each node
            #print("Node proba is: {}".format(node_proba))
            nodes_probs.append(node_proba)
            #print("Nodes probablities: {}".format(nodes_probs))
        random_proba_node = np.random.choice(G.nodes(),p=nodes_probs)
        #print("Randomly selected node is: {}".format(random_proba_node))
        return random_proba_node
    
    def add_edge():
            if len(G.edges()) == 0:
                random_proba_node = 0
            else:
                random_proba_node = rand_prob_node()
            new_edge = (random_proba_node, new_node)
            if new_edge in G.edges():
                print("\tThe edge connecting node {} and node {} already exists！".format(new_node + 1, random_proba_node))
                add_edge()
            else:
                #print("\t\t\t\t\tRight!")
                G.add_edge(new_node, random_proba_node)
                #print("Edge added: {} {}".format(new_node + 1, random_proba_node))
    
    count = 0
    new_node = init_nodes
    
    for f in range(final_nodes - init_nodes):
        #print("----------> Step {} <----------".format(count))
        G.add_node(init_nodes + count)
        #print("Node added: {}".format(init_nodes + count + 1))
        count += 1
        for e in range(0, m_parameter):
            add_edge()
        new_node += 1

    print("\nFinal number of nodes ({}) reached".format(len(G.nodes())))
    PhotoNumber = int(input("\nchoose Network Diagram by 1 or Scatter Diagram by 2 or Double logarithm processed scatter plot by 3 : "))
    if PhotoNumber==1:
        nx.draw(G, node_size=50, with_labels=0, alpha=0.6, node_color="#40a6d1", edge_color="#52bced")
        #plt.title("Visulation Of The Scale Free Network(Number: {})".format(len(G.nodes())))
    elif PhotoNumber==2:
        k_distrib(graph=G,colour='#40a6d1',alpha=.8)
    elif PhotoNumber==3:
        k_distrib(graph=G,colour='#40a6d1', scale='log',alpha=.8, expct_lo=3, expct_hi=14, expct_const=8)
    else:
        print("Wrong Input!")
        

elif chooseNumber==2:
    final_nodes2 = int(input("\nPlease type in the final number of nodes: "))
    m_parameter2 = int(input("\nPlease type in the least number of each nood connected: "))
    
    G2 = nx.Graph()
    
    print("Graph created. Number of nodes: {}".format(len(G2.nodes())))
    print("Adding nodes...")
    
    def rand_prob_node():
        random_proba_node = np.random.choice(G2.nodes())
        #print("Randomly selected node is: {}".format(random_proba_node))
        return random_proba_node
    
    def add_edge2():
            if len(G2.edges()) == 0:
                random_proba_node = 0
            else:
                random_proba_node = rand_prob_node()
            new_edge2 = (random_proba_node, new_node2)
            if new_edge2 in G2.edges():
                print("\tThe edge connecting node {} and node {} already exists！".format(new_node + 1, random_proba_node))
                add_edge2()
            else:
                #print("\t\t\t\t\tRight!")
                if (np.random.randint(0, 2)<1):
                    G2.add_edge(new_node2, random_proba_node)
                #print("Edge added: {} {}".format(new_node2 + 1, random_proba_node))
    
    count = 0
    new_node2 = 1
    for h in range(final_nodes2):
        G2.add_node(h)
        #print("Node added: {}".format(count + 1))
        count += 1
    print("Connect nodes...")
    for k in range(final_nodes2-1):
        for e in range(0, m_parameter2):
            add_edge2()
        new_node2 += 1
        
    print("\nFinal number of nodes ({}) reached".format(len(G2.nodes())))

    PhotoNumber2 = int(input("\nchoose Network Diagram by 1 or Scatter Diagram by 2: "))
    if PhotoNumber2==1:
        if len(G2.nodes())< 60:
            nx.draw(G2, node_size=40,width=2,with_labels=0, alpha=0.6, node_color="#40a6d1", edge_color="#CD2626")      
        else:
            plt.figure(figsize=(15, 15))
            nx.draw(G2, node_size=40, with_labels=0, alpha=0.6, node_color="#40a6d1", edge_color="#CD2626")
        #plt.title("Visulation Of The Scale Free Network(Number: {})".format(len(G.nodes())))
    elif PhotoNumber2==2:
        k_distrib(graph=G2,colour='#40a6d1',alpha=.8)
    else:
        print("Wrong Input!")
    
else:
    print("Wrong Input!")
     