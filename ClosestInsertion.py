import utilities as ut
import os 
import sys
import itertools as itol
import time
import matplotlib.pyplot as plt
import networkx as nx

filename = sorted(os.listdir('tsp_dataset'))[int(sys.argv[1])]
if (len(sys.argv)==2):
    a = ut.parseFile(filename)
    #print(a)

#solve the mst by adding to the partial path the node that is the nearest to the partial path
def closestInsertion(dmatrix):
    #init
    dim = len(dmatrix)
    partial = []
    remaining = list(range(dim))
    partial.append(0)
    remaining.remove(0)


    #stop the cicle when there are no more nodes to be added
    while remaining:

        toadd = -1
        mindist = 2147483647

        #get the node nearest to the partial graph
        for j in remaining:
            mindist2 = 2147483647
            for k in partial:
                if dmatrix[j,k] < mindist:
                    mindist2 = dmatrix[j,k]
            
            if mindist2 < mindist :
                toadd = j
                mindist = mindist2

        remaining.remove(toadd)

        nearest = 0
        valnearest = 21474836474
        
        #find the correct position in which insert the node 
        if len(partial) == 1:
                nearest=1
        else:
            for idx in range(len(partial)-1):
                t = dmatrix[toadd,idx] + dmatrix[toadd,idx+1] - dmatrix[idx,idx+1]
                if  t < valnearest:
                    valnearest = t
                    nearest = idx
            #check distance 0 and last element        
            if dmatrix[toadd,len(partial)-1] + dmatrix[toadd,0] - dmatrix[0,len(partial)-1] < valnearest:
                    nearest = len(partial)
        #now i know what node i have to add and where
        partial.insert(nearest, toadd)

        #TODO debug
        # G = nx.Graph()
        # plt.figure(3, figsize=(10,10))
        # if len(partial) > 1:
        #     for i, x, y in ut.parseFileCoords(filename):
        #         G.add_node(i, pos=(x,y))
        #     for i in range(len(partial)-1):
        #         G.add_edge(partial[i]+1, partial[i+1]+1)
        #     G.add_edge(partial[0]+1, partial[-1]+1)
        # pos=nx.get_node_attributes(G,'pos')
        # nx.draw(G, pos, node_size=15, with_labels=True)
        # plt.show()
    #print(partial)      

    #compute total path length
    distanceFinal =0
    for i in range(len(partial)-1):
        distanceFinal += dmatrix[partial[i],partial[i+1]]
    #add the distance of the last elemento to the first element to complete the circle
    distanceFinal += dmatrix[0, partial[-1]]

    return list(map(lambda x:x+1,partial)), distanceFinal

print('closest insertion: ', closestInsertion(a) )