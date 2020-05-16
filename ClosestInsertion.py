import utilities as ut
import os 
import sys
import itertools as itol
import time



# filename = sorted(os.listdir('tsp_dataset'))
# if (len(sys.argv)==2):
#     a = ut.parseFile(filename[int(sys.argv[1])])
#     #print(a)

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
                    nearest = idx + 1

        #now i know what node i have to add and where
        partial.insert(nearest, toadd)

    #print(partial)      

    #compute total path length
    distanceFinal =0
    for i in range(len(partial)-1):
        distanceFinal += dmatrix[partial[i],partial[i+1]]
    #add the distance of the last elemento to the first element to complete the circle
    distanceFinal += dmatrix[0, partial[-1]]

    return partial, distanceFinal

#print('closest insertion: ', closestInsertion(a) )