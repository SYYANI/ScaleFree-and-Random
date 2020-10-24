class Nood:
    def __init__(self):
        self.connectNum = 0

    def addNood(self, nood):
        self.connectNum += 1
        nood.connectNum += 1

def chooseNood(edges):
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

def chooseNood_2(edges):
    ranNum=random.randint(0,len(edges)-1)
    return edges[ranNum]

def draw(edges):
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


def draw_2(edges):
    numToconnection_dict = dict()
    numToconnection_dict_key = dict()
    while edges:
        lastNood = edges.pop()
        if lastNood.connectNum in numToconnection_dict.keys():
            numToconnection_dict[lastNood.connectNum] += 1
        else:
            numToconnection_dict[lastNood.connectNum] = 1
        
        

    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    ax.set_title("Scale Free Network",fontsize=24)
    ax.set_xlabel("Number of connections",fontsize=14)
    ax.set_ylabel("Number",fontsize=14)
    ax.scatter(numToconnection_dict.keys(), numToconnection_dict.values(), s=30)
    
    plt.show()

if __name__ == "__main__":
    import random
    import math
    import matplotlib.pyplot as plt

    edges = list()
    nood1, nood2 = Nood(), Nood()
    nood1.addNood(nood2)
    edges.append(nood1)
    edges.append(nood2)

    for i in range(4999):
        new_nood = Nood()
        chooseNood_2(edges).addNood(new_nood)
        edges.append(new_nood)

    draw(edges)
