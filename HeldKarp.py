import utilities as ut
import os 
import sys
import itertools as itol

filename = sorted(os.listdir('tsp_dataset'))
if (len(sys.argv)==2):
    a = ut.parseFile(filename[int(sys.argv[1])])
    #print(a)

##########
#HELD&KARP
##########
# Set like {1,2,3,4} can be encoded by 2^1 + 2^3 + 2^2 + 2^4 = 0b11110
# 2^3 can be calculated with bitwise shift: 2 << 3 
# a dictionary C is used where each key is a tuple (v,S) where S is the set encoded in binary
def calcHeldKarp(dmatrix):
    dim = len(dmatrix) 

    #inside C it saves all subset solutions
    C = { }

    for i in range(1, dim):
        C[(i, 1 << i)] = (dmatrix[i,0], 0)

    print(C)

    for j in range(2, dim):
        for subset in itol.combinations(range(1,dim), j):
            enc = 0
            #encode each city combination
            for bit in subset:
                enc |= 1 << bit

            #find the cheapest previus set to get to this subset
            for k in subset:
                #remove k from S and search on all these possibile sets
                prevsub = enc & ~ (1 << k)

                results= []
                for m in subset:
                    #the 0 node is the starting point so is ignored, also if j point is already traversed is ignored
                    if m==0 or m==k:
                        pass
                    # search for all possible paths and save them in results to then get the min cost path
                    else:
                        try:
                            results.append((C[(m, prevsub)][0] + dmatrix[m,k], m))
                        except:
                            printenc(C)
                            raise Exception('error accessing key', (m,prevsub), ' in C')

                C[(k, enc)] = min(results)    
    

    #now we search for the encoding containing all cities (0b11111...0) except the first
    final = 2**dim-2
    fresults = []

    for k in range(1,dim):
        #for each node of final combination (all nodes except 0) check distance to 0
        fresults.append((C[(k, final)][0] + dmatrix[k,0], k))
    
    opt, parent = min(fresults)

    #TODO missing path reconstruction
    return opt


#debugging function to see what sets are being considered
def printenc(C):
        for key,value in C.items():
            t = bin(key[1])
            sett = []
            num=0
            for i in t[::-1]:
                if i == 'b':
                    break
                num += 1
                if i == '1':
                    sett.append(str(num))
            print (key[0] , sett, ': ', value)




print(calcHeldKarp(a)) 

