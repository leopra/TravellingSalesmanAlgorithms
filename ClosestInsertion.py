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
        k = toadd
        pos = -1
        valnearest = 21474836474
        
        #find the correct position in which insert the node 
        if len(partial) == 1:
                nearest=1
        else:
            minimo=valnearest
            #dove inserire il nodo k dopo aver trovato la soluzione
            for i in range(0, len(partial)): #controllo le coppie di archi all'interno di C
                if i+1< len(partial):
                    val=dmatrix[partial[i],k] + dmatrix[k,partial[i+1]] - dmatrix[partial[i], partial[i+1]]
                    j=i+1
                    #print(val, toadd+1, partial[i], partial[i+1])
                else:
                    val=dmatrix[partial[i],k] + dmatrix[k,partial[0]] - dmatrix[partial[i], partial[0]]
                    j=0
                    #print(val, toadd+1, partial[i], partial[0])
                if val<minimo: 
                    minimo=val
                    pos=j


        #now i know what node i have to add and where
        partial.insert(pos, toadd)
        # if nearest+1 < len(partial):
        #     print('inserito: ', toadd+1 , 'in: ', pos ,'between', partial[pos-1]+1, partial[pos+1]+1 )
        #     print(list(map(lambda x:x+1,partial)))

        #TODO debug
        # G = nx.Graph()
        # plt.figure(3, figsize=(10,10))
        # if len(partial) > 1:
        #     for i, x, y in ut.parseFileCoords(filename):
        #         G.add_node(i, pos=(x,y))
        #     for i in range(len(partial)-1):
        #         G.add_edge(partial[i]+1, partial[i+1]+1, weigth = dmatrix[partial[i], partial[i+1]])
        #     G.add_edge(partial[0]+1, partial[-1]+1)
        # pos=nx.get_node_attributes(G,'pos')
        # nx.draw(G, pos, node_size=15, with_labels=True)
        # labels = nx.get_edge_attributes(G,'weight')
        # nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        # plt.show()
        # if nearest+1 < len(partial):
        #     print('inserito: ', toadd+1 , 'between', partial[nearest-1]+1, partial[nearest+1]+1 )

    #print(partial)      

    #compute total path length
    distanceFinal =0
    for i in range(len(partial)-1):
        distanceFinal += dmatrix[partial[i],partial[i+1]]
    #add the distance of the last elemento to the first element to complete the circle
    distanceFinal += dmatrix[0, partial[-1]]

    return list(map(lambda x:x+1,partial)), distanceFinal

print('closest insertion: ', )
s = time.time()
string = closestInsertion(a) 
e = time.time()

with open('ClosestInsertionResults.txt', 'a') as f:
    s = filename + '  ' +  str(e-s) + '  ' + str(int(string[1])) + '\n'
    f.write(s)