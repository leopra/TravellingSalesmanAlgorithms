import matplotlib.pyplot as plt
import networkx as nx
import utilities as ut
import os 
import sys
import itertools as itol
import time

# assert len(sys.argv) == 2
# filename = sorted(os.listdir('tsp_dataset'))[int(sys.argv[1])]
# a = ut.parseFile(filename)

# example = ut.parseFileCoords(filename)

######################################
# DRAW HELD KARP
# plt.figure(1)
# G = nx.Graph()
# for i, x, y in example:
#     G.add_node(i, pos=(x,y))

# path, length = HK.calcHeldKarpRecursiveVersion(a)

# for i in range(len(path)-1):
#     G.add_edge(path[i], path[i+1])
# #connect last to first    
# G.add_edge(path[0], path[-1])

# pos=nx.get_node_attributes(G,'pos')
# nx.draw(G, pos, node_size=20, with_labels=True)

# #######################################
# # DRAW CLOSEST INSERTION
# G = nx.Graph()
# plt.figure(2)
# for i, x, y in example:
#     G.add_node(i, pos=(x,y))

# path, length = ClIn.closestInsertion(a)

# for i in range(len(path)-1):
#     G.add_edge(path[i], path[i+1])
# #connect last to first    
# G.add_edge(path[0], path[-1])

# pos=nx.get_node_attributes(G,'pos')
# nx.draw(G, pos, node_size=20, with_labels=True)
# plt.show()


def drawPath(filename, arrayPaths):

    example = ut.parseFileCoords(filename)

    fig,axes = plt.subplots(1,len(arrayPaths), figsize=(25,10))
    ax= axes.flatten()
    index=0
    for j in arrayPaths:
        
        G = nx.Graph()
        for i, x, y in example:
            G.add_node(i, pos=(x,y))

        path = j
        for i in range(len(path)-1):
            G.add_edge(path[i], path[i+1])
        #connect last to first    
        G.add_edge(path[0], path[-1])

        pos=nx.get_node_attributes(G,'pos')
        nx.draw(G, pos, node_size=20, with_labels=True, ax=ax[index])
        index+=1

    if len(arrayPaths) == 3:
        ax[0].set_title('FARTHEST INSERTION')
        ax[1].set_title('CLOSEST INSERTION')
        ax[2].set_title('2APPROX')
    else:
        ax[0].set_title('HELD & KARP')
        ax[1].set_title('FARTHEST INSERTION')
        ax[2].set_title('CLOSEST INSERTION')
        ax[3].set_title('2APPROX')

    plt.show()
